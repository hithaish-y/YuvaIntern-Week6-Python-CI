# YuvaIntern Week 6 - CI Documentation

## Objective
This project demonstrates Continuous Integration (CI) for a Python application using GitHub Actions.

## Project Structure
- `secure_app.py` - secure Python user-management application
- `test_secure_app.py` - automated pytest test suite
- `requirements.txt` - Python dependencies
- `.flake8` - flake8 configuration
- `.github/workflows/ci.yml` - GitHub Actions CI pipeline
- `CI_DOCUMENTATION.md` - CI setup and replication instructions

## CI Pipeline
Every push or pull request triggers the workflow.

The pipeline:
1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs dependencies.
4. Runs flake8 for code-quality checking.
5. Runs pytest for automated testing.

If flake8 or pytest fails, the GitHub Actions job fails. This prevents a change with failing quality checks or tests from being treated as a successful CI build.

## Local Verification
Open a terminal in the project folder and run:

```text
pip install -r requirements.txt
flake8 .
pytest -q
```

The expected result is that flake8 completes without errors and pytest reports all tests as passed.

## How to Trigger CI
1. Create a GitHub repository.
2. Upload all project files while keeping `.github/workflows/ci.yml` in the same path.
3. Commit the files.
4. Open the repository's **Actions** tab.
5. GitHub Actions automatically starts the workflow after a push.
6. Make a small code or documentation change and commit again to demonstrate another CI run.

## Test Report
Pytest is used as the automated test framework. The tests cover username validation, email validation, password validation, password hashing, user creation, duplicate usernames, and invalid input handling.

## Challenges
The main setup challenges are maintaining the correct workflow path, installing compatible dependencies, and ensuring tests do not depend on a permanent database. The test suite uses a temporary database for isolation.

## Conclusion
The project demonstrates a repeatable CI workflow that automatically checks code quality and runs automated tests whenever changes are pushed or proposed through a pull request.


## Actual Verification Results

The project was verified locally after completing the CI setup.

- Flake8: Completed successfully with no reported issues.
- Pytest: 7 tests passed successfully.
- Application test: User creation and user search were tested successfully.
- The application runs correctly using Python 3.13.

### Final Status

All local quality checks and automated tests completed successfully. The project is ready for CI execution through GitHub Actions.