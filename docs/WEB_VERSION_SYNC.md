# DholeWeb = DholeSystem: version policy

Both repositories use the **same** semantic version per coordinated release. The source of truth is DholeSystem's `version.json` and `release-manifest.json`; DholeWeb `version.json`, `package.json`, the root entry of `package-lock.json` and changelogs must match it.

The System version-policy CI validates `components[DholeWeb].version == DholeSystem.version`. Web release CI also reads the target System branch (`develop` for staging and `master` for production) and rejects a mismatch. To release, update both candidate branches, integrate System into `develop`, then Web into `develop`, validate staging and CI, and only then promote the corresponding candidates to `master` with explicit production authorization. No changes to `main` are needed.

DholeWeb generates `/version.json` per build (SemVer, channel, commit). Open browser tabs check for a changed version or commit and display an update dialog; reload is always a user action, protecting unsaved forms. The endpoint is served with no-cache semantics. No new API, scopes, or authentication bypass are introduced.
