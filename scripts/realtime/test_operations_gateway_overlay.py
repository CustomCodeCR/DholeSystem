import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
COMPOSE = (ROOT / "deploy" / "docker-compose.services.yml").read_text()
ENV = (ROOT / "deploy" / "prepare-environments.sh").read_text()

class OperationsOverlayTests(unittest.TestCase):
    def test_gateway_has_rest_hub_and_health(self):
        self.assertIn('Gateway__Routes__15__Prefix: "/api/operations"', COMPOSE)
        self.assertIn('Gateway__Routes__16__Prefix: "/hubs/operations"', COMPOSE)
        self.assertIn('Gateway__HealthChecks__operations:', COMPOSE)
        self.assertIn('Gateway__Routes__16__StripPrefix: "false"', COMPOSE)

    def test_operations_defaults_on_both_generated_envs(self):
        self.assertIn('append_if_missing "$file" OPERATIONS_DB "dhole_operations"', ENV)
        self.assertIn('append_if_missing "$file" OPERATIONS_HTTP_URL "http://operations-api:8080"', ENV)
        self.assertIn('prepare_runtime_env "$PROD_ENV" "dhole"', ENV)
        self.assertIn('prepare_runtime_env "$STAGING_ENV" "dhole-staging"', ENV)

if __name__ == "__main__":
    unittest.main()
