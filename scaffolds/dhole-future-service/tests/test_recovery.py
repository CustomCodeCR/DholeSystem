"""F8 recovery: Redis re-delivery + durable SQL Inbox idempotency; CI only."""
import os
import uuid
import unittest
import psycopg
import redis

class Recovery(unittest.TestCase):
    def test_at_least_once_stream_and_postgres_inbox(self):
        dsn=os.environ.get("F8_TEST_POSTGRES")
        if not dsn: self.fail("F8_TEST_POSTGRES required")
        r=redis.Redis(host="localhost", port=16391, decode_responses=True)
        self.assertTrue(r.ping())
        event_id = uuid.uuid4()
        key="dhole.f8.ci.recovery"
        for _ in range(2):
            r.xadd(key, {"eventId":str(event_id), "payload":'{"eventType":"future.order.changed.v1"}'})
        self.assertEqual(r.xlen(key),2)
        with psycopg.connect(dsn) as db:
            added=0
            for _id,fields in r.xrange(key):
                with db.transaction():
                    result=db.execute(
                        "INSERT INTO future.inbox(event_id) VALUES(%s) ON CONFLICT DO NOTHING RETURNING event_id",
                        (fields["eventId"],)).fetchone()
                    added += int(result is not None)
            self.assertEqual(added,1,"Inbox must not apply same eventId twice")
            self.assertEqual(db.execute(
                "SELECT count(*) FROM future.inbox WHERE event_id=%s", (event_id,)).fetchone()[0],1)

if __name__ == "__main__":
    unittest.main()
