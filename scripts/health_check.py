"""Offline runtime and repository checks; never reads credentials."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]

def check(root=ROOT):
    config = tomllib.loads((root / "pyproject.toml").read_text())
    if not config.get("project", {}).get("name"):
        raise RuntimeError("Missing project name")
    if sys.version_info < (3, 11):
        raise RuntimeError("Python 3.11+ required")
    git = subprocess.run(["git", "--version"], check=True, capture_output=True, text=True)
    subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=root,
                   check=True, capture_output=True, text=True)
    for name in ("README.md", "AGENTS.md", "scripts/setup.sh", ".agents/skills"):
        if not (root / name).exists():
            raise RuntimeError(f"Missing required path: {name}")
    with tempfile.TemporaryDirectory(dir=root) as temp:
        probe = Path(temp) / "probe.txt"
        probe.write_text("workspace-write-check", encoding="utf-8")
        if probe.read_text(encoding="utf-8") != "workspace-write-check":
            raise RuntimeError("File round trip failed")
    return {"status": "PASS", "python": sys.version.split()[0],
            "git": git.stdout.strip(), "file_round_trip": "PASS",
            "dependencies": "standard library only"}

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
