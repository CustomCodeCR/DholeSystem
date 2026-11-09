# F4/F7 — Vue conflict revocation and resource lifecycle

2026-11-08. Release `rt-20261107-01`. Web/System/global candidate `1.13.1`.

## Change and evidence

The real Vue composable retained a remote conflict snapshot after authorization denial, allowed callbacks from a previous subscription after A→B→A navigation, and retained conflicts after scope disposal. Three behavioral tests reproduced all three failures before the fix. Generation checks now reject obsolete callbacks and denial/disposal clears retained conflict data. The browser singleton is replaced only in the Node fixture; the actual Vue effect scope and production composable execute. This is not staging evidence.

- Original Web SHA: `ad115d2d66b09f35a5340857168a84dd7ca8442f`.
- Committed fix: [`8ac693125c3be20ea23f5bab757fff4b449908e4`](https://github.com/CustomCodeCR/DholeWeb/commit/8ac693125c3be20ea23f5bab757fff4b449908e4).
- `node --test tests/realtimeResourceBinding.test.mjs tests/realtimeF4Manager.test.ts`: 28 passed, 0 failed, 0 skipped.
- `pnpm run type-check`: exit 0.
- `pnpm run build`: exit 0, realtime flags default OFF; Vite plugin timing warnings present.
- Full Node suite: 665 tests, 632 passed, 33 failed, 0 skipped.
- Same full suite on an isolated original HEAD: 659 tests, 632 passed, the same 33 failures, 0 skipped. No new failure names.
- F0: 17 source branches retrieved; detailed queue 512 mutable HTTP candidates + 70 workers; 57 additional overlapping signatures. None represents a completed manual mapping.

No formal phase is approved by this change. Staging WSS/ACL, Redis migration/restore, remaining producer/view coverage, all formal F7 scenarios, branch enforcement and the coordinated F9/F10 integration remain unfinished.

## Existing suite failures blocking a clean release

- AI recommendation is bounded by Average and can never modify cost
- Anticipado / Redestino are persisted and applied to pricing condition
- Draft auto-apply distributes sale changes from the existing sale structure instead of dumping them into freight
- FASE 54 keeps editor modal and drawer surfaces scrollable on constrained viewports
- FASE 55 keeps modal drawer Block Picker and Media Picker reachable with long content
- FCL keeps already-persisted individual weights
- FCL refresh reconciles generic plus persisted container freight into exactly one freight
- FCL refresh retains one freight per two different equipment types
- Month drag and week/day half-hour drops persist via optimistic concurrency
- Pantalla 7 exposes Average suggestion before the final draft and keeps cost immutable
- Pricing + Vendedor roles expose both dashboard views, not only SuperUsuario
- Prospect can be searched and selected for calendar appointments
- Sale overrides are linked to source cost without changing cost in Pricing
- a seller modification restores saved LCL freight instead of losing it
- delivery confirmation is emitted only by explicit send actions
- legacy seller FCL: 15,000 kg aggregate restores the missing single 40HC weight
- multi-FCL refresh also retains charges from an additional selected carrier
- multi-agent configured cost remains valid when the selected agent is not its legacy first agent
- own LCL screen 7 recalculates every matrix item, preserves detail IDs, and retains manual charges
- pricing queue disables send action until preparation is persisted
- screen 7 preserves every persisted line if Pricing returns no matching amounts
- screen 7 recalculates sale and includes only the seller-selected port handling
- screen 7 refreshes a persisted cost even when the wizard generates zero lines
- screen 7 replaces RS/ONE historical charges with WWL/MSC and marks obsolete details for deletion
- seller detail uses resolved currency for both header and commercial lines
- seller modification allows only one in-flight save per wizard instance
- tests/crmPreferentialCostGroups.test.ts
- tests/crmPreferentialCostRoute.test.ts
- tests/crmPreferentialTierSales.test.ts
- tests/pricingCarrierHaulageAnyMode.test.ts
- tests/pricingExwFcaVariableCosts.test.ts
- the caller records whether a Pricing API request was attempted
- the read-only Pricing route renders master screen 9, not a summary drawer

## Review correction

Independent scoped review found a delayed REST response could repopulate data after revocation. Two manager tests (clean/dirty editor) and another composable test reproduced it. The manager now rejects denied watcher results after await; the composable invalidates its generation on denial. All 28 realtime tests pass. This resolves the important review finding; the full release is still incomplete.

## Framework verification

.NET SDK 8.0.427 installed locally. `dotnet test tests/CustomCodeFramework.Messaging.Realtime.Tests/CustomCodeFramework.Messaging.Realtime.Tests.csproj --no-restore --nologo -m:1`: 44 passed, 0 failed/skipped. Existing XML documentation warnings remain. Parallel MSBuild exited without diagnostic errors in this host; serial execution succeeds. No framework source changes.

Full Web suites were compared after building each checkout, because one preexisting test requires the generated bundle. Before building, that missing-bundle test adds one failure to each suite. After building, baseline 626/659 and patched 632/665 pass, with identical 33 failure names.
