"""Synthetic negative/positive regression tests for F0 source reconciliation."""
import unittest

from f0_consolidate_review import reconcile, signature

SHA = "b" * 40
BASE = {
    "repo": "CustomCodeCR/DholeCRMService",
    "sourceFile": "src/Endpoints/Accounts.cs",
    "kind": "MUTABLE_HTTP_CANDIDATE",
    "sourceLine": "42", "verb": "PATCH",
    "routeSegment": "/accounts/{id}",
}
GAP = {
    "repo": "CustomCodeCR/DholeCRMService",
    "sourceFile": "src/Endpoints/Accounts.cs",
    "kind": "DYNAMIC_MUTABLE_ROUTE",
    "line": "55", "sourceHint": "MapMethods(dynamicRoute, verbs)",
}
HEAD = [{"repo": BASE["repo"], "shaAtScan": SHA}]


def approved(key, sha=SHA, **changes):
    row = {
        "sourceKey": key, "sourceSha": sha, "status": "VALIDATED",
        "reviewer": "reviewer", "reviewedAtUtc": "2026-11-08T21:00:00Z",
        "resourceOwner": "CRM", "effectiveRouteOrJob": "PATCH /api/crm/accounts/{id}",
        "authorizationPolicy": "Resource owner ACL",
        "eventContract": "crm.account.updated.v1", "audience": "account:{id}",
        "frontendConsumer": "CrmRecordDetailView",
        "restReconcile": "GET /api/crm/accounts/{id}",
        "integrationTest": "test_crm_account_patch",
        "evidenceUrl": "https://github.com/CustomCodeCR/DholeCRMService/actions/runs/123",
        "approvedBy": "owner", "approvalEvidence": "https://github.com/CustomCodeCR/DholeSystem/pull/123",
    }
    row.update(changes)
    return row


class ReviewTests(unittest.TestCase):
    def test_stable_source_identity(self):
        self.assertEqual(signature(BASE, "F6_PRIMARY")["sourceKey"],
                         signature(dict(BASE), "F6_PRIMARY")["sourceKey"])

    def test_dynamic_routes_not_silently_deduplicated(self):
        rows, errors = reconcile([BASE], [GAP], HEAD, [])
        self.assertFalse(errors)
        self.assertEqual(len(rows), 2)
        self.assertEqual(sum(x["possibleSameFileOverlap"] != "NO" for x in rows), 1)
        self.assertTrue(all(x["reviewStatus"] == "UNVERIFIED" for x in rows))

    def test_review_approved_at_exact_source_sha(self):
        key = signature(BASE, "F6_PRIMARY")["sourceKey"]
        rows, errors = reconcile([BASE], [], HEAD, [approved(key)])
        self.assertFalse(errors)
        self.assertEqual(rows[0]["reviewStatus"], "EVIDENCE_SUBMITTED_VALIDATED")

    def test_stale_sha_fails_closed(self):
        key = signature(BASE, "F6_PRIMARY")["sourceKey"]
        rows, errors = reconcile([BASE], [], HEAD, [approved(key, sha="a"*40)])
        self.assertEqual(rows[0]["reviewStatus"], "UNVERIFIED")
        self.assertTrue(any("STALE_SHA" in e for e in errors))

    def test_missing_acl_rejected(self):
        key = signature(BASE, "F6_PRIMARY")["sourceKey"]
        rows, errors = reconcile([BASE], [], HEAD, [approved(key, authorizationPolicy="")])
        self.assertEqual(rows[0]["reviewStatus"], "UNVERIFIED")
        self.assertTrue(any("authorizationPolicy" in e for e in errors))

    def test_exception_requires_approval(self):
        key = signature(BASE, "F6_PRIMARY")["sourceKey"]
        rows, errors = reconcile([BASE], [], HEAD, [
            approved(key, status="EXEMPT", exceptionReason="", approvalEvidence="")
        ])
        self.assertEqual(rows[0]["reviewStatus"], "UNVERIFIED")
        self.assertTrue(errors)

    def test_unknown_or_duplicate_decision_rejected(self):
        key = signature(BASE, "F6_PRIMARY")["sourceKey"]
        rows, errors = reconcile([BASE], [], HEAD, [
            approved(key), approved(key), approved("unexpected")
        ])
        self.assertEqual(rows[0]["reviewStatus"], "EVIDENCE_SUBMITTED_VALIDATED")
        self.assertEqual(len(errors), 2)

    def test_missing_head_must_not_pass(self):
        rows, errors = reconcile([BASE], [], [], [])
        self.assertEqual(len(rows), 1)
        self.assertTrue(any("No scanned branch SHA" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
