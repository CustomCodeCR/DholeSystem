CREATE SCHEMA IF NOT EXISTS future;
CREATE TABLE IF NOT EXISTS future.orders (
  id uuid PRIMARY KEY,
  owner_id text NOT NULL,
  status text NOT NULL CHECK(status IN ('Pending','Approved','Cancelled')),
  version bigint NOT NULL CHECK(version > 0),
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS future.outbox (
  event_id uuid PRIMARY KEY,
  aggregate_id uuid NOT NULL REFERENCES future.orders(id),
  owner_id text NOT NULL,
  payload jsonb NOT NULL CHECK(jsonb_typeof(payload) = 'object'),
  created_at timestamptz NOT NULL DEFAULT now(),
  attempts integer NOT NULL DEFAULT 0,
  processed_at timestamptz
);
CREATE INDEX IF NOT EXISTS future_outbox_unpublished
 ON future.outbox(created_at,event_id) WHERE processed_at IS NULL;
CREATE TABLE IF NOT EXISTS future.inbox (
  event_id uuid PRIMARY KEY,
  processed_at timestamptz NOT NULL DEFAULT now()
);
