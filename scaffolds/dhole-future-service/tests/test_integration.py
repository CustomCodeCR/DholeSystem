"""F8 integration evidence: real PostgreSQL transaction and constraints, not UI/ACL E2E."""
import os
import unittest
import psycopg

class FutureOutboxPostgres(unittest.TestCase):
    def setUp(self):
        self.dsn = os.environ.get("F8_TEST_POSTGRES")
        if not self.dsn:
            self.fail("F8_TEST_POSTGRES is required; do not report SKIPPED")
        self.connection = psycopg.connect(self.dsn)

    def tearDown(self):
        self.connection.close()

    def test_rollback_reverts_outbox_and_owner_data(self):
        with self.connection.cursor() as cur:
            cur.execute("SELECT count(*) FROM future.orders")
            baseline = cur.fetchone()[0]
        import uuid
        oid = uuid.uuid4()
        with self.assertRaises(RuntimeError):
            with self.connection.transaction():
                self.connection.execute(
                    "INSERT INTO future.orders(id,owner_id,status,version) VALUES(%s,%s,'Pending',1)",
                    (oid, "f8-transaction",))
                self.connection.execute(
                    "INSERT INTO future.outbox(event_id,aggregate_id,owner_id,payload) VALUES(%s,%s,%s,%s)",
                    (uuid.uuid4(), oid, "f8-transaction", '{"eventType":"future.order.changed.v1"}'))
                raise RuntimeError("simulate commit failure before ACK")
        self.connection.rollback()
        with self.connection.cursor() as cur:
            cur.execute("SELECT count(*) FROM future.orders")
            self.assertEqual(cur.fetchone()[0], baseline)
            cur.execute("SELECT count(*) FROM future.outbox WHERE aggregate_id=%s", (oid,))
            self.assertEqual(cur.fetchone()[0], 0)

    def test_optimistic_revision_and_scope_sql(self):
        import uuid
        oid=uuid.uuid4()
        with self.connection.transaction():
            self.connection.execute(
                "INSERT INTO future.orders(id,owner_id,status,version) VALUES(%s,%s,'Pending',1)",
                (oid, "f8-owner"))
        with self.connection.transaction():
            self.connection.execute(
                "UPDATE future.orders SET version=version+1 WHERE id=%s AND owner_id=%s AND version=1",
                (oid, "f8-not-owner"))
        with self.connection.cursor() as cur:
            cur.execute("SELECT version FROM future.orders WHERE id=%s", (oid,))
            self.assertEqual(cur.fetchone()[0], 1)
        with self.connection.transaction():
            self.connection.execute(
                "UPDATE future.orders SET version=version+1 WHERE id=%s AND owner_id=%s AND version=1",
                (oid, "f8-owner"))
        with self.connection.cursor() as cur:
            cur.execute("SELECT version FROM future.orders WHERE id=%s", (oid,))
            self.assertEqual(cur.fetchone()[0], 2)
        with self.connection.transaction():
            self.connection.execute(
                "UPDATE future.orders SET version=version+1 WHERE id=%s AND owner_id=%s AND version=1",
                (oid, "f8-owner"))
        with self.connection.cursor() as cur:
            cur.execute("SELECT version FROM future.orders WHERE id=%s", (oid,))
            self.assertEqual(cur.fetchone()[0], 2)

if __name__ == "__main__":
    unittest.main()
