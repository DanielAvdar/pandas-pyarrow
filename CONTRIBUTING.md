# Contribution Guidelines
Thank you for your interest in contributing to SchemArrow.

## Prerequisites
Before you start, make sure you have **poetry** installed on your machine. You can install it with this command:

```bash
pip install poetry
```

Also, make sure you have **forked** the repository and **cloned** your fork to your local machine.

## Setup
To set up the project, navigate to the project directory and run these commands:

Install the project dependencies
```bash
poetry install
```
Install the pre-commit hooks
```bash
poetry run pre-commit install
```

## Testing and Code Checking
To run the tests, use this command:

```bash
poetry run pytest
```

To check the code style and formatting, use this command:

```bash
poetry run pre-commit run --all-files
```
