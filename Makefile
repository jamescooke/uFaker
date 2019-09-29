# TODO add setup.py
lint_files=src/ufaker tests

.PHONY: lint
lint:
	@echo "=== flake8 ==="
	flake8 $(lint_files)
	@echo "=== mypy ==="
	mypy $(lint_files)
	@echo "=== isort ==="
	isort --quiet --recursive --diff $(lint_files) > .isort.out
	if [ "$$(wc -l .isort.out)" != "0 .isort.out" ]; then cat .isort.out; exit 1; fi
	@echo "=== black ==="
	black --target-version py36 --check --diff $(lint_files)
	@printf "\nSUCCESS\n\n"

.PHONY: fixlint
fixlint:
	@echo "=== fixing isort ==="
	isort --quiet --recursive $(lint_files)
	@echo "=== fixing black ==="
	black --target-version py36  $(lint_files)

.PHONY: clean
clean:
	find . -name *.pyc -delete
	find . -name __pycache__ -delete
