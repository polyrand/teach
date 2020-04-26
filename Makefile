<SRC = $(wildcard ./*.ipynb)
DIR = .
ROOTDIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DOCKERFILE =  Dockerfile
ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
.DEFAULT_GOAL := build

help:
> @echo "clean - remove all build, test, coverage and Python artifacts"
> @echo "clean-build - remove build artifacts"
> @echo "clean-pyc - remove Python file artifacts"

.PHONY: clean
clean:
> rm -rf `find . -name __pycache__`
> rm -f `find . -type f -name '*.py[co]' `
> rm -f `find . -type f -name '*~' `
> rm -f `find . -type f -name '.*~' `
> rm -rf .cache
> rm -rf .pytest_cache
> rm -rf htmlcov
> rm -rf *.egg-info
> rm -f .coverage
> rm -f .coverage.*
> rm -rf build/
> rm -rf dist/
> rm -fr .eggs/
> find . -name '*.egg-info' -exec rm -fr {} +
> find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-build
clean-build:
> rm -fr build/
> rm -fr dist/
> rm -fr .eggs/
> find . -name '*.egg-info' -exec rm -fr {} +
> find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc:
> find . -name '*.pyc' -exec rm -f {} +
> find . -name '*.pyo' -exec rm -f {} +
> find . -name '*~' -exec rm -f {} +
> find . -name '__pycache__' -exec rm -fr {} +

.PHONY: deps
deps: $(shell find requirements -name '*.in' -type f)
> pip install pip-tools pip setuptools
> pip-compile -v --build-isolation --generate-hashes --allow-unsafe --output-file requirements/main.txt requirements/main.in
> pip-compile -v --build-isolation --generate-hashes --allow-unsafe --output-file requirements/dev.txt requirements/dev.in

.PHONY: update-deps
update-deps:
> pip install --upgrade pip-tools pip setuptools
> pip-compile -v --upgrade --build-isolation --generate-hashes --allow-unsafe --output-file requirements/main.txt requirements/main.in
> pip-compile -v --upgrade --build-isolation --generate-hashes --allow-unsafe --output-file requirements/dev.txt requirements/dev.in
