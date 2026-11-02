import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("health", Path(__file__).resolve().parents[1] / "scripts/health_check.py")
health = importlib.util.module_from_spec(spec)
spec.loader.exec_module(health)

class HealthTests(unittest.TestCase):
    def test_real_workspace(self):
        self.assertEqual(health.check()["status"], "PASS")

    def test_incomplete_workspace_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(FileNotFoundError):
                health.check(Path(temp))

if __name__ == "__main__":
    unittest.main()
