#!/bin/bash


isort --check-only .
black . --check
flake8 .
vulture . --min-confidence 70
mypy .
