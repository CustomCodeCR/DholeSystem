using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Npgsql;
using StackExchange.Redis;

var pg = Environment.GetEnvironmentVariable("F8_TEST_POSTGRES")
    ?? throw new InvalidOperationException("F8_TEST_POSTGRES required");
var command = args.Length == 1 ? args[0] : throw new ArgumentException("seed|publish|redeliver");
var db = NpgsqlDataSource.Create(pg);
if (command == "seed")
{
    var id = Guid.NewGuid();
    await using var connection = await db.OpenConnectionAsync();
    await using var tx = await connection.BeginTransactionAsync();
    await using var cmd = new NpgsqlCommand("""
        INSERT INTO future.orders(id,owner_id,status,version) VALUES (@id,'f8-owner','Pending',1)
        """, connection, tx);
    cmd.Parameters.AddWithValue("id", id);
    await cmd.ExecuteNonQueryAsync();
    await FutureOutbox.AppendAsync(connection, tx, id, "f8-owner", 1, CancellationToken.None);
    await tx.CommitAsync();
    Console.WriteLine("F8_OWNER_AND_OUTBOX_ATOMIC_COMMIT_OK");
}
else if (command == "redeliver")
{
    await using var cmd = db.CreateCommand("""
        UPDATE future.outbox SET processed_at=NULL WHERE owner_id='f8-owner'
        """);
    await cmd.ExecuteNonQueryAsync();
    Console.WriteLine("F8_SIMULATE_FAILURE_AFTER_STREAM_BEFORE_DB_MARK");
}
else if (command == "publish")
{
    var multiplexer = await ConnectionMultiplexer.ConnectAsync("127.0.0.1:16391");
    using var host = Host.CreateDefaultBuilder()
        .ConfigureLogging(x => x.SetMinimumLevel(LogLevel.Warning))
        .ConfigureServices(s =>
        {
            s.AddSingleton(db);
            s.AddSingleton<IConnectionMultiplexer>(multiplexer);
            s.AddHostedService<OutboxWorker>();
        }).Build();
    await host.StartAsync();
    var processed = false;
    for (var attempt = 0; attempt < 60; attempt++)
    {
        await Task.Delay(150);
        await using var status = db.CreateCommand("""
            SELECT count(*) FROM future.outbox WHERE owner_id='f8-owner' AND processed_at IS NULL
            """);
        if (Convert.ToInt64(await status.ExecuteScalarAsync()) == 0)
        {
            processed = true;
            break;
        }
    }
    await host.StopAsync();
    await multiplexer.CloseAsync();
    if (!processed) throw new Exception("Outbox not drained");
    Console.WriteLine("F8_REAL_PUBLISHER_OUTBOX_DRAINED");
}
else throw new ArgumentException("Unknown mode");
