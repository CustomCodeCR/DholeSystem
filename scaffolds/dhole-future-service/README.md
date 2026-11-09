# Dhole future service scaffold — F8 candidate

This repository subtree is a compilable test example, not a running Dhole
microservice or an approved fourteenth service. It demonstrates scope and
resource-owner REST protection, optimistic concurrency, atomic PostgreSQL
Outbox, Redis Streams publisher, event identity, telemetry and SQL Inbox
deduplication. The central Hub remains in DholeApiGateway.

Generate a new service candidate from DholeSystem's intermediate branch:

    python scripts/realtime/scaffold-future-service.py \
      --name DholeBillingService --domain billing --service-id S14 \
      --owner PlatformTeam --version 1.13.0 --out /tmp/DholeBillingService

The destination must not already exist. The generated output contains source,
manifest, SQL, contract and recovery tests, local policy verifier, CI workflow
and a central-registry.PROPOSAL.yaml file. Review and add the proposal to
DholeSystem's service-registry.yaml in its own intermediate release branch;
the proposal is not an authorized registration or a deployment.

The generated CI requires an organization-approved, read-only secret
DHOLE_REGISTRY_READ_TOKEN. It fetches the authoritative DholeSystem develop
registry and **fails** without it. Only during F9 (after batch merge) may
the registry snapshot become authoritative for a real future service.

The manifest guard identifies literal C# MapPost/Put/Patch/Delete and hosted
workers; unsupported MapMethods or route generation fails closed pending
separate review. Source scanning is not runtime proof. Execute contract,
PostgreSQL, Redis recovery, real authenticated ACL, two-user WSS and fallback
tests, check no data leaks, and have security reviewer sign the evidence.

The source sample includes an at-least-once publisher; an actual new service
still needs production DLQ orchestration, real durable Inbox consumer wiring,
client view bindings and central Gateway stream registration. No alternate
SignalR Hub or second browser socket is authorized.

Never deploy during F0-F8. Keep feature flags OFF until the F9/F10 release
batch and enforce required GitHub PR status checks in protected branches.
