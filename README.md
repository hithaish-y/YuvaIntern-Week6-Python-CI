# YuvaIntern Week 6 - Python CI

A Python project demonstrating Continuous Integration with GitHub Actions.

## Features
- Secure password hashing
- Input validation
- SQLite user management
- Automated pytest tests
- Flake8 code-quality checks
- GitHub Actions CI pipeline

## Run Locally

```text
pip install -r requirements.txt
flake8 .
pytest -q
python secure_app.py
```

## CI
The workflow in `.github/workflows/ci.yml` runs on every push and pull request. It installs dependencies, checks code quality with flake8, and runs the pytest test suite.

See `CI_DOCUMENTATION.md` for complete setup and replication instructions.
