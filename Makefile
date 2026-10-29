.DEFAULT_GOAL := help

CARGO ?= cargo
PYTHON ?= python3

.PHONY: help all build-rv build-la check verify-imports

help:
	@echo "Repository scaffold; bootable kernels are not implemented yet."
	@echo "make check           - Check the dependency-free Rust library on the host"
	@echo "make verify-imports  - Verify imported source hashes"
	@echo "make all             - Reserved evaluator entry point (currently fails)"

all: build-rv build-la

build-rv build-la:
	@echo "ERROR: $@ is not implemented; startup code and linker scripts are pending." >&2
	@echo "See docs/architecture.md and the workspace Doc/tasks.md roadmap." >&2
	@exit 2

check:
	$(CARGO) check --workspace --locked --offline

verify-imports:
	$(PYTHON) scripts/verify-imports.py
