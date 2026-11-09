using System.Diagnostics.Metrics;
using System.Text.Json;
using Microsoft.Extensions.Hosting;
using Npgsql;
using StackExchange.Redis;

public static class FutureOutbox
{
    public static async Task AppendAsync(NpgsqlConnection db, NpgsqlTransaction tx,
        Guid id, string owner, long version, CancellationToken ct)
    {
        var eventId = Guid.NewGuid();
        var payload = JsonSerializer.Serialize(new
        {
            eventId, eventType = "future.order.changed.v1", schemaVersion = 1,
            aggregateType = "order", aggregateId = id.ToString("D"),
            aggregateVersion = version, occurredAtUtc = DateTimeOffset.UtcNow,
            producer = "DholeFutureSample", correlationId = eventId.ToString("D"),
            audienceRef = "future:order:" + id.ToString("D"),
            payload = new { changedFields = new[] {"status"} }
        });
        await using var cmd = new NpgsqlCommand("""
            INSERT INTO future.outbox(event_id, aggregate_id, owner_id, payload)
            VALUES(@event,@id,@owner,@payload::jsonb)
            """, db, tx);
        cmd.Parameters.AddWithValue("event", eventId);
        cmd.Parameters.AddWithValue("id", id);
        cmd.Parameters.AddWithValue("owner", owner);
        cmd.Parameters.AddWithValue("payload", payload);
        await cmd.ExecuteNonQueryAsync(ct);
    }
}

/// <summary>
/// The owner commits business rows and Outbox together. A crash AFTER XADD and
/// BEFORE marking processed can republish the same eventId; central Gateway's
/// durable Inbox must dedupe. Never use SignalR to mutate business state.
/// </summary>
public sealed class OutboxWorker(NpgsqlDataSource db, IConnectionMultiplexer redis,
    ILogger<OutboxWorker> log) : BackgroundService
{
    private static readonly Meter Metrics = new("Dhole.FutureSample.Realtime");
    private static readonly Counter<long> Sent = Metrics.CreateCounter<long>("dhole.realtime.events.sent");
    private static readonly Counter<long> Failed = Metrics.CreateCounter<long>("dhole.realtime.events.failed");
    private const string Stream = "dhole.future-sample.realtime.v1";
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            try
            {
                await using var connection = await db.OpenConnectionAsync(stoppingToken);
                await using var tx = await connection.BeginTransactionAsync(stoppingToken);
                await using var cmd = new NpgsqlCommand("""
                    SELECT event_id, payload::text FROM future.outbox
                    WHERE processed_at IS NULL ORDER BY created_at,event_id
                    LIMIT 100 FOR UPDATE SKIP LOCKED
                    """, connection, tx);
                var batch = new List<(Guid Id, string Json)>();
                await using (var reader = await cmd.ExecuteReaderAsync(stoppingToken))
                {
                    while (await reader.ReadAsync(stoppingToken))
                        batch.Add((reader.GetGuid(0), reader.GetString(1)));
                }
                foreach (var evt in batch)
                {
                    await redis.GetDatabase().StreamAddAsync(Stream,
                        [new NameValueEntry("eventId", evt.Id.ToString("D")),
                         new NameValueEntry("payload", evt.Json)]);
                    await using var mark = new NpgsqlCommand("""
                        UPDATE future.outbox SET processed_at=now(),attempts=attempts+1
                        WHERE event_id=@event AND processed_at IS NULL
                        """, connection, tx);
                    mark.Parameters.AddWithValue("event", evt.Id);
                    await mark.ExecuteNonQueryAsync(stoppingToken);
                    Sent.Add(1);
                }
                await tx.CommitAsync(stoppingToken);
                if (batch.Count == 0)
                    await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);
            }
            catch (OperationCanceledException) when (stoppingToken.IsCancellationRequested)
            {
                return;
            }
            catch (Exception exc)
            {
                Failed.Add(1);
                log.LogWarning(exc, "future sample Outbox will retry after transport failure");
                await Task.Delay(TimeSpan.FromSeconds(2), stoppingToken);
            }
        }
    }
}
