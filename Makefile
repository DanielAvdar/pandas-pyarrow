.PHONY: help
.PHONY: default
default: install

install:
	poetry install --all-extras
#	poetry run pre-commit autoupdate
	poetry run pre-commit install

test:
	poetry run pytest

check:
	poetry run pre-commit run --all-files
mypy:
	poetry run mypy . --config-file pyproject.toml
coverage:
	poetry run pytest --cov=ml_orchestrator --cov-report=xml
