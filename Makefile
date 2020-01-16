SRC = $(PWD)/src
TESTS = $(PWD)/tests

PYTHON = python3
REQUIREMENTS = $(SRC)/requirements.txt
STAGE = dev

.PHONY: unit test coverage clean tdd debug

deps: .deps
.deps: $(REQUIREMENTS) requirements.txt
	pip install -r requirements.txt
	pip install -r $(REQUIREMENTS)
	touch .deps

clean:
	@echo "Cleaning all artifacts..."
	@-rm -rf _build
	@-rm -rf _temp
	@-rm .deps

ipython: deps
	$(PYTHON) -m IPython

unit test: deps
	$(PYTHON) -m pytest ../tests

tdd: deps
	$(PYTHON) -m pytest --stepwise $(TESTS)

new: test
	$(PYTHON) util/fetch_problem.py

debug: deps
	$(PYTHON) -m pytest --stepwise -vv --pdb $(TESTS)

coverage: deps
	$(PYTHON) -m pytest ../tests --cov $(SRC) --cov-report=term-missing ../tests
