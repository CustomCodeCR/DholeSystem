using System.Security.Claims;
using System.Text.Json;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Npgsql;
using StackExchange.Redis;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.Authority = builder.Configuration["Auth:Authority"]
            ?? throw new InvalidOperationException("Auth:Authority required");
        o.Audience = builder.Configuration["Auth:Audience"]
            ?? throw new InvalidOperationException("Auth:Audience required");
        o.RequireHttpsMetadata = true;
    });
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("future.orders.view",
        p => p.RequireAuthenticatedUser().RequireClaim("scope", "future.orders.view"));
    options.AddPolicy("future.orders.write",
        p => p.RequireAuthenticatedUser().RequireClaim("scope", "future.orders.write"));
});
var pg = builder.Configuration.GetConnectionString("DholeFuture")
    ?? throw new InvalidOperationException("DholeFuture Postgres connection required");
var redis = builder.Configuration.GetConnectionString("RedisStreams")
    ?? throw new InvalidOperationException("RedisStreams connection required");
builder.Services.AddSingleton(_ => NpgsqlDataSource.Create(pg));
builder.Services.AddSingleton<IConnectionMultiplexer>(_ => ConnectionMultiplexer.Connect(redis));
builder.Services.AddHostedService<OutboxWorker>();
var app = builder.Build();
app.UseAuthentication();
app.UseAuthorization();

var orders = app.MapGroup("/api/future/orders");
// Scope AND per-owner row authorization; a gateway REST check must never
// trust a client-provided SignalR group or an event payload.
orders.MapGet("/{id:guid}", async (Guid id, ClaimsPrincipal user,
    NpgsqlDataSource db, CancellationToken ct) =>
{
    var subject = user.FindFirstValue(ClaimTypes.NameIdentifier) ?? user.FindFirstValue("sub");
    if (string.IsNullOrWhiteSpace(subject)) return Results.Forbid();
    await using var cmd = db.CreateCommand("""
        SELECT id,version,status FROM future.orders WHERE id=@id AND owner_id=@owner
        """);
    cmd.Parameters.AddWithValue("id", id);
    cmd.Parameters.AddWithValue("owner", subject);
    await using var reader = await cmd.ExecuteReaderAsync(ct);
    return await reader.ReadAsync(ct)
        ? Results.Ok(new { id = reader.GetGuid(0), version = reader.GetInt64(1),
                           status = reader.GetString(2) })
        : Results.NotFound();
}).RequireAuthorization("future.orders.view");

orders.MapPost("/", async (CreateOrder request, HttpContext http,
    NpgsqlDataSource db, CancellationToken ct) =>
{
    var subject = http.User.FindFirstValue(ClaimTypes.NameIdentifier)
        ?? http.User.FindFirstValue("sub");
    if (string.IsNullOrWhiteSpace(subject)) return Results.Forbid();
    if (request.Id == Guid.Empty) return Results.BadRequest();
    await using var connection = await db.OpenConnectionAsync(ct);
    await using var tx = await connection.BeginTransactionAsync(ct);
    await using var cmd = new NpgsqlCommand("""
        INSERT INTO future.orders(id,owner_id,status,version)
        VALUES (@id,@owner,'Pending',1) ON CONFLICT DO NOTHING RETURNING id
        """, connection, tx);
    cmd.Parameters.AddWithValue("id", request.Id);
    cmd.Parameters.AddWithValue("owner", subject);
    var inserted = await cmd.ExecuteScalarAsync(ct);
    if (inserted is null) return Results.Conflict("Order exists");
    await FutureOutbox.AppendAsync(connection, tx, request.Id, subject, 1, ct);
    await tx.CommitAsync(ct);
    return Results.Created("/api/future/orders/" + request.Id, new { request.Id });
}).RequireAuthorization("future.orders.write");

orders.MapPatch("/{id:guid}", async (Guid id, PatchOrder request, HttpContext http,
    NpgsqlDataSource db, CancellationToken ct) =>
{
    var subject = http.User.FindFirstValue(ClaimTypes.NameIdentifier)
        ?? http.User.FindFirstValue("sub");
    if (string.IsNullOrWhiteSpace(subject)) return Results.Forbid();
    if (request.ExpectedVersion <= 0 || !new[] {"Pending","Approved","Cancelled"}.Contains(request.Status))
        return Results.BadRequest();
    await using var connection = await db.OpenConnectionAsync(ct);
    await using var tx = await connection.BeginTransactionAsync(ct);
    await using var cmd = new NpgsqlCommand("""
        UPDATE future.orders SET status=@status, version=version+1
        WHERE id=@id AND owner_id=@owner AND version=@expected
        RETURNING version
        """, connection, tx);
    cmd.Parameters.AddWithValue("id", id);
    cmd.Parameters.AddWithValue("owner", subject);
    cmd.Parameters.AddWithValue("status", request.Status);
    cmd.Parameters.AddWithValue("expected", request.ExpectedVersion);
    var value = await cmd.ExecuteScalarAsync(ct);
    if (value is null) return Results.Conflict("Missing, forbidden or stale version");
    var version = Convert.ToInt64(value);
    await FutureOutbox.AppendAsync(connection, tx, id, subject, version, ct);
    await tx.CommitAsync(ct);
    return Results.Ok(new { id, version, request.Status });
}).RequireAuthorization("future.orders.write");

app.MapGet("/health", () => Results.Ok(new { status = "healthy" }));
app.Run();

public sealed record CreateOrder(Guid Id);
public sealed record PatchOrder(long ExpectedVersion, string Status);
