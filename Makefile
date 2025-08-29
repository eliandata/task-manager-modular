.PHONY: fmt lint test

fmt:
	black .
	isort .

lint:
	flake8 .

test:
	pytest -q
