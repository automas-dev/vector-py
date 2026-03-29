
setup:
	uv sync

build:
	uv build

install: build
	/usr/bin/python3 -m pip install dist/$$(ls dist | grep .whl | tail -n 1)

checks: lint test

lint:
	uv run ruff format --check
	uv run ruff check .

format:
	uv run ruff format
	uv run ruff check --fix .

test:
	uv run pytest tests

.PHONY: setup build install checks lint format test
