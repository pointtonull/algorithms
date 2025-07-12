$(warning [DEPRECATED] Makefile is deprecated; please use 'just' instead)
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
	$(PYTHON) -m pytest $(TESTS)

tdd: deps ## run tests on filesystem events
	ptw $(SRC) $(TESTS) --runner "$(PYTHON) -m pytest --capture=fd --stepwise --tb=short $(TESTS)"

new: test
	$(PYTHON) util/fetch_problem.py

debug: deps ## run tests on filesystem events, open pdb on failures
	ptw $(SRC) $(TESTS) --pdb --runner "$(PYTHON) -m pytest --stepwise $(TESTS)"

coverage: deps
	$(PYTHON) -m pytest tests --cov $(SRC) --cov-report=term-missing:skip-covered tests

help:  ## Show this help message
	@echo "\033[1mUsage:\033[0m"
	@echo "  just [recipe]\n"
	@echo "\033[1mTargets:\033[0m"
	@awk -F ":.*?## " -v und="\033[2mundocumented\033[0m" '\
		/^[A-z][^:\t ]+:/&&NF==2{\
			printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2 | "sort"\
		}\
		/^[A-z][^:\t ]+:/&&NF==1{\
			split($$1, a, ":");\
			printf "  \033[36m%-12s\033[0m %s\n", a[1], und | "sort"\
		}' $(MAKEFILE_LIST)
