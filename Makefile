#
# Copyright (c) 2022 by Delphix. All rights reserved.
#
.PHONY: --check_python --check_env_exists run tests --create_virtual_env --install_dependencies env clean_build clean_env clean build

ROOT_DIR := $(shell pwd)
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
DLPX_NR := $(ROOT_DIR)/dist/delphix-nr

define show_version
	@export LC_ALL=en_AU.UTF-8; $(DLPX_NR) --version
endef

define check_python_exists
	@if ! command -v python3.8 -V >/dev/null 2>&1; then \
		echo "Python 3.8 is NOT present on the system, Please install it"; \
		exit 1; \
	fi
endef


--check_python:
	@# Help: Checks existence of python virtual environment
	$(call check_python_exists)

--check_env_exists: --check_python
	@[ -f $(PYTHON) ] && echo $(PYTHON) exists || (echo $(PYTHON) does NOT exist, use \"make env\" to create a virtual env; exit 1)


run: --check_env_exists
	@# Help: Takes care of checking the prequisites like python, virtual env, dependencies and at last shows the Python Version
	-@echo `$(PYTHON) -V`
	export PYTHONPATH=$(ROOT_DIR); $(PYTHON) src/main.py

tests:
	@# Help: Runs the unit tests inside tests folder and create a report
	$(PYTHON) -m pytest tests -s -v

--create_virtual_env: --check_python
	@# Help: Creates a virtual environment
	-@echo 'Creating Virtual environment'
	@python3.8 -m venv venv || echo 'Python env already exists'

--install_dependencies: requirements.txt
	@# Help: Installs the dependencies from requirements.txt
	-@echo 'Installing Dependencies...'
	@$(PYTHON) -m pip install --upgrade pip
	@$(PIP) install -r requirements.txt

env: --create_virtual_env --install_dependencies
	@# Help: Creates a virtual environment with python3.8 if not already present and activates it

clean_env:
	@# Help: Clean the virtual env that was created
	-@$(VENV)/bin/pre-commit uninstall
	-@rm -rf venv

clean_build:
	@# Help: Cleans the build files
	-@rm -rf build/
	-@rm -rf dist/
	-@rm -rf delphix-nr.spec

clean: clean_build
	@# Help: Cleans the pycache, coverage and build files
	-@rm -rf __pycache__
	-@rm -f .coverage
	-@rm -rf .pytest_cache
	-@rm -rf tests/.pytest_cache
	-@rm -rf tests/plugin_operations/.pytest_cache
	-@rm -rf tests/CodeCoverage
	-@rm -rf tests/Report.html
	-@rm -rf .dvp-gen-output

build: --check_env_exists clean_build
	@# Help: Makes the delphix-nr build
	$(VENV)/bin/pyinstaller --onefile src/main.py -n delphix-nr
	-@echo 'Build is present at $(ROOT_DIR)/dist/delphix-nr'
	$(call show_version)


# A hidden target
.hidden:
help:
	@printf "%-20s %s\n" "Target" "Description"
	@printf "%-20s %s\n" "------" "-----------"
	@make -pqR : 2>/dev/null \
        | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' \
        | sort \
        | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' \
        | xargs -I _ sh -c 'printf "%-20s " _; make _ -nB | (grep -i "^# Help:" || echo "") | tail -1 | sed "s/^# Help: //g"'
