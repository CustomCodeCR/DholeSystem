#!/usr/bin/env python3
"""Audit existing SignalR, WebSocket proxy and Redis Compose (no QA users needed).
Source/Compose checks are not runtime TLS, ACL or data-restoration evidence.
"""
import argparse
import json
from pathlib import Path
import re
import sys
import yaml


def must(condition, label):
    if not condition:
        raise ValueError("Missing existing infrastructure invariant: " + label)


def verify(workspace):
    def source(repo, path):
        return (workspace / repo / path).read_text(encoding="utf-8-sig")
    gateway = source("DholeApiGateway", "Dhole.ApiGateway/Program.cs")
    proxy = source("DholeApiGateway", "Dhole.ApiGateway/Gateway/GatewayProxyMiddleware.cs")
    notifications = source("DholeNotificationsService", "src/Dhole.Notifications.Api/Program.cs")
    web = source("DholeWeb", "src/core/realtime/notificationRealtime.ts")
    universal = source("DholeWeb", "src/core/realtime/universalRealtime.ts")
    infra = yaml.safe_load(source("DholeSystem", "deploy/docker-compose.staging-infra.yml"))
    services = yaml.safe_load(source("DholeSystem", "deploy/docker-compose.services.yml"))
    staging = yaml.safe_load(source("DholeSystem", "deploy/docker-compose.staging.yml"))
    must("app.UseWebSockets();" in gateway, "Gateway UseWebSockets")
    must("ProxyWebSocketAsync" in proxy and "IsWebSocketRequest" in proxy,
         "Gateway WebSocket proxy")
    must("AddSignalR()" in notifications and
         'MapHub<NotificationsHub>("/api/notifications/hub")' in notifications,
         "NotificationsHub existing")
    must("/api/notifications/hub" in web and "wss:" in web and
         "requestHubTicket" in web and "new WebSocket(" in web,
         "DholeWeb Notifications WSS client")
    must("MapHub<UniversalRealtimeHub>" in gateway and
         "if (universalRealtimeEnabled)" in gateway and
         "Realtime:BatchApproved" in gateway,
         "new universal hub remains feature-gated")
    must("VITE_DHOLE_REALTIME_BATCH_APPROVED" in universal,
         "Web universal hub feature gate")
    redis = infra["services"]["redis"]
    command = redis["command"]
    must(isinstance(command, list) and "--appendonly" in command and
         command[command.index("--appendonly") + 1] == "yes" and
         "--appendfsync" in command and
         command[command.index("--appendfsync") + 1] == "everysec",
         "Redis AOF Compose declaration")
    must("dhole-staging-redis:/data" in redis["volumes"] and
         "dhole-staging-redis" in infra["volumes"], "Redis persistent volume")
    must("dhole-staging-postgres:/var/lib/postgresql/data" in
         infra["services"]["postgres"]["volumes"], "PostgreSQL persistent volume")
    flags = services["services"]["api-gateway"]["environment"]
    required = ("Features__UniversalRealtimeEnabled", "Realtime__Enabled",
                "Realtime__BatchApproved", "Realtime__BridgeEnabled",
                "Realtime__UniversalServicesBridgeEnabled")
    must(all(isinstance(flags.get(k), str) and
             re.search(r"\$\{[A-Z_0-9]+:-false\}", flags[k]) for k in required),
         "all universal flags default OFF")
    must("127.0.0.1:18080:8080" in staging["services"]["api-gateway"]["ports"],
         "staging Gateway bound to loopback")
    return {
        "releaseId": "rt-20261107-01",
        "sourceContract": "existing notification SignalR + gateway WS proxy + browser WSS",
        "existingNotificationHub": True,
        "newUniversalHubFeatureGated": True,
        "redisAofAndPersistentVolumesDeclared": True,
        "offlineQaAccountsRequired": False,
        "liveExternalWssVerified": False,
        "liveRedisAofAndRestoreVerified": False,
        "noRuntimeChanges": True,
        "formalGateApproved": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default="F0Results/working")
    parser.add_argument("--output", default="F0Results/F0-existing-ws-compose.json")
    args = parser.parse_args()
    try:
        report = verify(Path(args.workspace))
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2) + "\n")
    except (OSError, KeyError, ValueError, IndexError, TypeError, yaml.YAMLError) as exc:
        print("F0_EXISTING_WS_COMPOSE_BLOCKED:", exc, file=sys.stderr)
        return 2
    print("F0_EXISTING_WS_COMPOSE_PASS: existing SignalR, proxy and AOF config; runtime not inferred")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
