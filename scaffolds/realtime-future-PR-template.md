# Future Dhole microservice — realtime enrollment

- [ ] Service intermediate branch only, semver version and CHANGELOG updated.
- [ ] New owner/stream/Hub registration committed to DholeSystem registry (not just local registry PROPOSAL).
- [ ] Every mutating HTTP handler and background job in realtime.manifest.yaml.
- [ ] Resource owner, scope, audience, REST snapshot, Outbox, Inbox, retry and DLQ covered.
- [ ] C# source/API and database transaction prove business mutation + Outbox atomicity.
- [ ] No new Hub/SignalR client; use central DholeApiGateway and REST reconciliation.
- [ ] Positive/negative F8 policy CI; PG/Redis outage-recovery integration CI links attached.
- [ ] Two real users + one unauthorized scope tested; 0 leaks and 0 duplicated effects.
- [ ] Security reviewer, service owner and CODEOWNERS approval present.
- [ ] No direct develop/master/main write; F9/F10 only after all F0-F8 formal gates.

Owner: ____________________
Security reviewer: ____________________
CI run + SHA: ____________________
Coverage rows approved/total: ____________________
