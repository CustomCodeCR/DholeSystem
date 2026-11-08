#!/usr/bin/env python3
"""F8: fail-closed policy for new Dhole services, not approval for F0-F7.

Scans source for literal ASP.NET mutable Map* routes and BackgroundService
handlers. Every discovery needs an exact manifest mapping (or reviewed ADR).
Source scanning alone never counts as an integration/authorization test.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

import yaml

RELEASE = "rt-20261107-01"
BRANCH = "feature/dhole-realtime-universal-rt-20261107-01"
VERBS = {"POST", "PUT", "PATCH", "DELETE"}
METHOD_CALL = re.compile(r'\bMap(Post|Put|Patch|Delete|Methods)\s*\(', re.S)
ROUTE = re.compile(r'\bMap(Post|Put|Patch|Delete|Methods)\s*\(\s*"([^"]+)"', re.S)
WORKER = re.compile(r'\bclass\s+\w+[^\{;]*:\s*[^\{;]*(?:BackgroundService|IHostedService)\b', re.S)
SEMVER = re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$')
EVENT = re.compile(r'^[a-z][a-z0-9.-]+\.v[1-9][0-9]*$')
SOURCE = re.compile(r'^(src/)[A-Za-z0-9_./-]+\.cs$')
TEST = re.compile(r'^(tests/)[A-Za-z0-9_./-]+\.(?:cs|py)$')
TEXT = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.:/{}-]{1,256}$')
PLACEHOLDERS = ("TODO", "TBD", "PENDING", "NO_VERIFICADO", "REPLACE", "EXAMPLE")

def filled(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip()) and not any(
        value.upper().startswith(t) for t in PLACEHOLDERS)

def path_inside(root: Path, relative: str, *, check=SOURCE) -> Path:
    if not isinstance(relative, str) or not check.fullmatch(relative) or ".." in relative.split("/"):
        raise ValueError("Untrusted source/test path: " + str(relative))
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        raise ValueError("Missing or unsafe source/test file: " + relative)
    return target

def key(source: str, verb: str, path: str) -> tuple[str, str, str]:
    return (source, verb.upper(), path)

def source_inventory(root: Path) -> tuple[set[tuple[str, str, str]], set[str], list[str]]:
    discovered: set[tuple[str, str, str]] = set()
    workers: set[str] = set()
    problems: list[str] = []
    for file in sorted((root / "src").rglob("*.cs")):
        if any(s in {"obj", "bin", ".git"} for s in file.relative_to(root).parts):
            continue
        source = file.relative_to(root).as_posix()
        data = file.read_text(encoding="utf-8-sig")
        matches = list(ROUTE.finditer(data))
        calls = list(METHOD_CALL.finditer(data))
        if len(calls) != len(matches):
            problems.append(source + ": nonliteral Map* mutation/MapMethods requires explicit review")
        for hit in matches:
            verb, route = hit.group(1).upper(), hit.group(2)
            if verb == "METHODS":
                # Without parsing the verb array, the route must be rejected. A
                # MapMethods can hide POST/PATCH/DELETE under unusual formatting.
                problems.append(source + ": MapMethods needs explicit method parser/ADR: " + route)
                continue
            discovered.add(key(source, verb, route))
        if WORKER.search(data):
            workers.add(source)
        if re.search(r'\bMapHub\s*(?:<|\()', data):
            problems.append(source + ": new Hub is prohibited; use DholeApiGateway")
    return discovered, workers, problems

def validate(root: Path, *, registry: Path | None = None) -> list[str]:
    errors: list[str] = []
    path = root / "realtime.manifest.yaml"
    if not path.is_file():
        return ["realtime.manifest.yaml missing"]
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (yaml.YAMLError, OSError) as exc:
        return ["Cannot parse realtime.manifest.yaml: " + str(exc)]
    if not isinstance(doc, dict):
        return ["Realtime manifest must be an object"]
    if doc.get("schemaVersion") != 1 or doc.get("releaseId") != RELEASE:
        errors.append("schemaVersion/releaseId incorrect")
    service = doc.get("service")
    if not isinstance(service, dict):
        return errors + ["service object missing"]
    for field in ("id", "name", "repo", "owner", "version"):
        if not filled(service.get(field)):
            errors.append("service." + field + " missing/placeholder")
    if not SEMVER.fullmatch(str(service.get("version", ""))):
        errors.append("service.version must be SemVer")
    if not str(service.get("repo", "")).startswith("CustomCodeCR/"):
        errors.append("service.repo must be under CustomCodeCR")
    if doc.get("hub") != "DholeApiGateway":
        errors.append("Only central DholeApiGateway Hub is allowed")
    if doc.get("eventTransport") != "redis-streams":
        errors.append("eventTransport must be redis-streams")
    if doc.get("sourceOfTruth") != "REST":
        errors.append("REST must be the source of truth")
    for field in ("outbox", "inbox", "authorization", "observability", "recovery"):
        record = doc.get(field)
        if not isinstance(record, dict):
            errors.append(field + " object missing")
            continue
        mandatory = {
            "outbox": ("store", "sameTransactionAsMutation", "publisher", "retry", "dlq"),
            "inbox": ("store", "idempotencyKey", "ackAfterCommit"),
            "authorization": ("scopeEnforcedOnOwner", "resourceAclViaRest", "revalidateOnDelivery"),
            "observability": ("metrics", "structuredLogs", "correlationId"),
            "recovery": ("onReconnectRestRefresh", "offlineRestFallback")
        }[field]
        for k in mandatory:
            value = record.get(k)
            if isinstance(value, bool):
                if not value: errors.append(field + "." + k + " must be true")
            elif not filled(value):
                errors.append(field + "." + k + " missing/placeholder")
    try:
        discovered, workers, scan_problems = source_inventory(root)
    except (OSError, UnicodeError) as exc:
        return errors + ["Cannot scan sources: " + str(exc)]
    errors += scan_problems
    mutations = doc.get("mutations")
    if not isinstance(mutations, list):
        return errors + ["mutations list missing"]
    declared: set[tuple[str, str, str]] = set()
    approved_exceptions: set[tuple[str, str, str]] = set()
    exemptions = doc.get("exceptions", [])
    if not isinstance(exemptions, list):
        errors.append("exceptions must be a list")
        exemptions = []
    for entry in exemptions:
        if not isinstance(entry, dict):
            errors.append("invalid exception entry")
            continue
        try:
            operation = key(entry["source"], entry["verb"], entry["routeLiteral"])
            if entry.get("approved") is not True:
                errors.append("Unapproved exception: " + str(operation))
                continue
            adr = entry.get("signedAdr")
            reviewer = entry.get("approvedBy")
            expiry = entry.get("expiresOn")
            if not filled(reviewer) or not isinstance(adr, str) or not adr.startswith("docs/ADRs/"):
                errors.append("Exception missing independent owner and signed ADR")
                continue
            adr_path = (root / adr).resolve()
            if not adr_path.is_relative_to(root.resolve()) or not adr_path.is_file():
                errors.append("Exception ADR missing")
                continue
            if not isinstance(expiry, date) or expiry < date.today():
                errors.append("Exception date expired or missing")
                continue
            approved_exceptions.add(operation)
        except (KeyError, TypeError):
            errors.append("Malformed exception")
    for row in mutations:
        if not isinstance(row, dict):
            errors.append("malformed mutation entry")
            continue
        try:
            operation = key(row["source"], row["verb"], row["routeLiteral"])
            path_inside(root, row["source"])
        except (KeyError, ValueError) as exc:
            errors.append("Invalid mutation source: " + str(exc))
            continue
        if operation in declared:
            errors.append("duplicate declaration: " + str(operation))
        declared.add(operation)
        if operation[1] not in VERBS:
            errors.append("invalid HTTP verb: " + str(operation))
        for k in ("resourceOwner", "resourceKind", "eventType",
                  "audiencePolicy", "restSnapshot", "frontendConsumer",
                  "scope", "transactionalOutbox", "contractTest",
                  "integrationTest", "recoveryTest"):
            if not filled(row.get(k)):
                errors.append("Missing mutation " + k + ": " + str(operation))
        if not EVENT.fullmatch(str(row.get("eventType", ""))):
            errors.append("Event must be versioned: " + str(operation))
        for t in ("contractTest", "integrationTest", "recoveryTest"):
            try:
                path_inside(root, str(row.get(t, "")), check=TEST)
            except ValueError:
                errors.append("Missing test source " + t + ": " + str(operation))
        if row.get("restSnapshot", "").startswith("ws"):
            errors.append("No WebSocket authoritative snapshots allowed")
        if row.get("resourceOwner") != service.get("name"):
            errors.append("Mutation must identify exact owning service: " + str(operation))
    for operation in sorted(discovered - declared - approved_exceptions):
        errors.append("Unmapped mutable route " + str(operation))
    for operation in sorted(declared - discovered):
        errors.append("Stale/imaginary route in manifest " + str(operation))
    for operation in sorted(approved_exceptions - discovered):
        errors.append("Stale exception " + str(operation))
    job_entries = doc.get("jobs", [])
    if not isinstance(job_entries, list):
        errors.append("jobs must be a list")
        job_entries = []
    jobs: set[str] = set()
    for job in job_entries:
        if not isinstance(job, dict):
            errors.append("invalid jobs entry")
            continue
        src = job.get("source")
        try:
            path_inside(root, src)
        except ValueError:
            errors.append("Missing job source")
            continue
        if src in jobs:
            errors.append("duplicate worker " + src)
        jobs.add(src)
        for field in ("eventType", "scope", "audiencePolicy", "outbox",
                      "inbox", "contractTest", "recoveryTest"):
            if not filled(job.get(field)):
                errors.append("Worker missing " + field + ": " + src)
        for t in ("contractTest", "recoveryTest"):
            try:
                path_inside(root, str(job.get(t, "")), check=TEST)
            except ValueError:
                errors.append("Missing worker test " + t + ": " + src)
    for worker in sorted(workers - jobs):
        errors.append("Unmapped background worker " + worker)
    for worker in sorted(jobs - workers):
        errors.append("Stale/imaginary background worker " + worker)
    if registry is not None:
        try:
            reg = yaml.safe_load(registry.read_text(encoding="utf-8"))
            future = reg.get("futureServices", [])
            matching = [s for s in future if s.get("id") == service.get("id")
                        and s.get("repo") == service.get("repo")]
            if len(matching) != 1:
                errors.append("Future service must have exactly one central registry entry")
            else:
                item = matching[0]
                if item.get("stream") != doc.get("stream"):
                    errors.append("Future service registry stream mismatch")
                if item.get("hub") != "DholeApiGateway":
                    errors.append("Registry cannot create a second Hub")
        except (OSError, yaml.YAMLError, AttributeError):
            errors.append("Cannot validate central registry")
    if not filled(doc.get("stream")) or not re.fullmatch(
        r'dhole\.[a-z][a-z0-9.-]+\.realtime\.v[1-9]\d*', str(doc.get("stream", ""))):
        errors.append("Stream must be namespaced/versioned")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--service-root", required=True)
    parser.add_argument("--registry")
    args = parser.parse_args()
    failures = validate(Path(args.service_root), registry=Path(args.registry) if args.registry else None)
    for problem in failures:
        print("F8_POLICY_BLOCKED: " + problem, file=sys.stderr)
    if failures:
        print("F8_POLICY_FAIL_COUNT=" + str(len(failures)), file=sys.stderr)
        return 1
    print("F8_POLICY_PASS: every literal mutable endpoint and hosted worker mapped; "
          "registry and test source references validated (NOT formal staging approval)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
