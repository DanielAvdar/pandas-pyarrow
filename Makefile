.PHONY: help
.PHONY: default
default: install

install:
	poetry install --all-extras --all-groups
#	poetry run pre-commit autoupdate
	poetry run pre-commit install

test:
	poetry run pytest

check:
	poetry run pre-commit run --all-files
mypy:
	poetry run mypy pandas_pyarrow --config-file pyproject.toml
coverage:
	poetry run pytest --cov=pandas_pyarrow --cov-report=xml --junitxml=junit.xml -o junit_family=legacy
doc:
	poetry run sphinx-build -M html docs/source docs/build/
