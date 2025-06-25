# Justfile

SRC := justfile_directory() + "/src"
TESTS := justfile_directory() + "/tests"

PYTHON := "uv run python"
REQUIREMENTS := SRC + "/requirements.txt"
STAGE := "dev"

# Default recipe - show help
default:
    @just help

# Dependencies

# Sync dependencies using uv
deps:
    uv sync
    touch .deps

# Install project in development mode  
install:
    uv sync --dev
    touch .deps

# Clean

clean:
    echo "Cleaning all artifacts..."
    rm -rf _build _temp .deps

# Interactive Python

ipython: deps
    {{PYTHON}} -m IPython

# Unit Tests

test: deps
    {{PYTHON}} -m pytest {{TESTS}}

# TDD

tdd: deps
    uv run ptw {{SRC}} {{TESTS}} --runner "uv run pytest --capture=fd --stepwise --tb=short {{TESTS}}"

# Retrieve New Problem

new: test
    {{PYTHON}} util/fetch_problem.py

# Debug

debug: deps
    uv run ptw {{SRC}} {{TESTS}} --pdb --runner "uv run pytest --stepwise {{TESTS}}"

# Coverage

coverage: deps
    uv run pytest tests --cov=src --cov-report=term-missing:skip-covered

# Help

help:
    echo "Usage:"
    echo "  just [recipe]"
    echo "Recipes:"
    echo "  deps     Sync dependencies with uv"
    echo "  install  Install project in development mode"
    echo "  clean    Remove all build artifacts"
    echo "  ipython  Start an IPython shell"
    echo "  test     Run unit tests"
    echo "  tdd      Run tests on filesystem events"
    echo "  new      Retrieve a new problem"
    echo "  debug    Run tests with a debugger"
    echo "  coverage Check test coverage"
    echo "  help     Show this help message"

