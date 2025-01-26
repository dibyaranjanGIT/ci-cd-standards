# Code Standards for Python using GitHub Actions

This repository implements code quality and standards checks for Python projects using the following tools:

- **pydoc**: To ensure proper documentation of Python functions and classes.
- **codespell**: To catch common misspellings in code comments, variable names, and documentation.
- **black**: A Python code formatter that enforces consistent code style.
- **flake8**: A tool for linting Python code to enforce PEP 8 compliance and catch potential issues.

## How It Works

This repository uses **GitHub Actions** to automatically run these tools whenever code is pushed or a pull request is created. If any issues are found, the action will fail, and you will need to fix the issues before merging.

## Tools Setup

### pydoc
- Ensures that functions, classes, and modules have proper docstrings.
- Checks for adherence to Python's documentation best practices.

### codespell
- Detects and corrects typos in code, comments, and documentation.
- Can be configured to ignore specific words using a `.codespellignore` file.

### black
- Formats Python code to a consistent style.
- Automatically fixes formatting issues, so you only need to focus on functionality.

### flake8
- Lints Python code to ensure compliance with PEP 8 standards.
- Can be extended using plugins (e.g., flake8-docstrings).

## Prerequisites

Ensure you have the following installed locally if you want to run the tools manually:

- Python 3.7 or later
- Install dependencies with:
  ```bash
  pip install pydocstyle codespell black flake8
  ```

## GitHub Actions Workflow

A pre-configured GitHub Actions workflow is included in `.github/workflows/code_quality.yml`. This workflow runs the following checks:

1. **codespell**: Detects common misspellings.
2. **black**: Formats the code and checks for consistency.
3. **flake8**: Lints the code for style violations.
4. **pydocstyle**: Validates that all public methods, functions, and classes are properly documented.

### Example Workflow File

```yaml
name: Code Standards Check

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  code-quality:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        pip install codespell black flake8 pydocstyle

    - name: Run codespell
      run: codespell .

    - name: Run black
      run: black --check .

    - name: Run flake8
      run: flake8 .

    - name: Run pydocstyle
      run: pydocstyle .
```

## Running Locally

To check your code locally, you can run the tools manually:

1. **codespell**:
   ```bash
   codespell .
   ```

2. **black**:
   ```bash
   black --check .
   ```
   (Use `black .` to auto-format your code.)

3. **flake8**:
   ```bash
   flake8 .
   ```

4. **pydocstyle**:
   ```bash
   pydocstyle .
   ```

## Configuration Files

### .flake8
Customize Flake8 rules by creating a `.flake8` file in your repository:
```ini
[flake8]
max-line-length = 88
ignore = E203, W503  # Ignore certain rules (e.g., black compatibility)
```

### .codespellignore
Ignore specific words by creating a `.codespellignore` file:
```
behaviour
eanalyse
```

## Pull Request Checks

When you create a pull request, GitHub Actions will automatically run the code quality checks. If any check fails, you must resolve the issues before merging the pull request.

## Contribution Guidelines

1. Ensure your code passes all checks locally before committing.
2. Write proper docstrings for all public functions, methods, and classes.
3. Run `black` to format your code and fix style issues.
4. Check for typos using `codespell`.
5. Submit your changes only after all checks pass.

---

With this setup, your codebase will maintain a high standard of quality, ensuring clean, well-documented, and consistent Python code.
