# Cloud environment validation

Run from the existing repository checkout with Python 3.11+, Git, Bash, and venv:

```bash
bash scripts/setup.sh
python3 scripts/health_check.py
python3 -m unittest discover -s tests -v
```

The onboarding Cloud instance on 2026-11-03 passed setup, the health check,
and both unit tests using Python 3.12.14 and Git 2.52.0. Setup was rerun
successfully and left tracked files unchanged. No third-party packages,
paid services, YouTube skills, deployments, or live trading were used.

These results validate the onboarding instance. After publishing the environment,
repeat the commands in a fresh Cloud task to verify snapshot restoration.
GitHub access must be checked separately through the platform's authenticated
HTTPS proxy; successful offline tests do not establish GitHub write access.
