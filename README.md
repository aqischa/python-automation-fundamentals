# Python Automation Fundamentals

A collection of Python fundamentals and automation exercises developed as part of my Test Automation and DevOps upskilling journey.

## Overview

This project focuses on building practical Python skills for automation, testing and scripting.

### What I Practiced

- Python functions and modules
- Basic automation logic
- Server status checking
- Automated testing with `pytest`
- Git and GitHub workflow
- CI using GitHub Actions

## Project Structure

```text
python-automation-fundamentals/
├── fundamentals/
│   └── server_checker.py
├── tests/
│   └── test_server_checker.py
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── requirements.txt
└── README.md
```

## Running the Tests

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest
```

## CI/CD

This project uses **Github Actions** to automatically run the pytest test suite when changes are pushed to `main` or when a pull request targets `main`.

The workflow:

1. Checks out the repository
2. Sets up Python 3.13
3. Installs dependencies
4. Runs the automated tests
5. Reports the test result

The CI pipeline was also tested by intentionally introducing a failing test and verifying that Github Actions correctly detected the failure before fixing it.

## Purpose

This project is part of my ongoing development towards **Test Automation, DevOps Engineering** roles.
