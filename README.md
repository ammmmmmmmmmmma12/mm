# First Dollar Development Workspace

Free, reproducible development infrastructure for **اول دولار من النت باستخدام دولار واحد**.
The repository was initialized from an empty repository. YouTube skills are not installed.

## Quick start

Requires Python 3.11+, Git, Bash, and Python venv support.

```bash
bash scripts/setup.sh
python3 scripts/health_check.py
python3 -m unittest discover -s tests -v
```

Setup creates a local .venv and runs offline health checks and tests. There are no
third-party Python dependencies, API keys, paid services, or requirements.txt needed.
Rerunning setup is supported. It does not install system packages or change Git identity.

## Structure

- AGENTS.md: persistent instructions and budget boundaries
- .agents/skills/: reserved for future reviewed skills
- scripts/: reproducible setup and runtime checks
- tests/: environment validation
- projects/: separate YouTube, trivia, digital product, Shopify, and trading projects
- docs/CODEX_SETUP.md: proposed Cloud settings and pending acceptance test

## Validation scope

Health checks verify Python, Git, project metadata, required files, and a real file
write/read round trip. They do not prove GitHub authentication or Codex Cloud task execution.
Cloud acceptance must be performed in a signed-in Codex environment.

No deployment, content publication, live trading, or paid usage is authorized by this setup.
