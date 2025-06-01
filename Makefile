.PHONY: help
.PHONY: default
default: install

install:
	uv sync --all-extras --all-groups --frozen
	uvx pre-commit install

update:
	uv lock
	uvx pre-commit autoupdate
	$(MAKE) install

test: install
	uv run pytest

check: install
	uvx pre-commit run --all-files

mypy: install
	uv run mypy pandas_pyarrow --config-file pyproject.toml

coverage: install
	uv run pytest --cov=pandas_pyarrow --cov-report=xml --junitxml=junit.xml -o junit_family=legacy

cov: install
	uv run pytest --cov=pandas_pyarrow --cov-report=term-missing

install-docs:
	uv sync --group docs --frozen --no-group dev

doctest: install-docs doc

doc:
	uv run --no-sync sphinx-build -M html docs/source docs/build/ -W --keep-going --fresh-env

check-all: check test mypy doc
