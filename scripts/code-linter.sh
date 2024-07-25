#!/usr/bin/env bash

clear
echo "Starting code linter"

RESULTS_FILE_NAME="code-linter.results.log"
SCRIPT_DIR="$(dirname -- "$0∂")"
PROJECT_DIR="$(dirname -- "$0∂")/.."
SOURCE_DIR="backend"

echo "$PROJECT_DIR"

RESULTS_FILE=$SCRIPT_DIR/../$RESULTS_FILE_NAME

MAX_LINE_LENGTH=120

echo 'Linter run at' > $RESULTS_FILE
date >> $RESULTS_FILE

echo "Running isort"
echo "Running isort" >> $RESULTS_FILE
isort "$PROJECT_DIR"/project/  >> $RESULTS_FILE

echo "Running flake8"
echo "Running flake8" >> $RESULTS_FILE
flake8 "$PROJECT_DIR"/$SOURCE_DIR/ --max-line-length=$MAX_LINE_LENGTH >> $RESULTS_FILE

echo "Running pycodestyle"
echo "Running pycodestyle" >> $RESULTS_FILE
pycodestyle "$PROJECT_DIR"/$SOURCE_DIR/ --max-line-length=$MAX_LINE_LENGTH >> $RESULTS_FILE

echo "Running Black"
echo "Running Black" >> $RESULTS_FILE
pycodestyle "$PROJECT_DIR"/$SOURCE_DIR/ --max-line-length=$MAX_LINE_LENGTH >> $RESULTS_FILE

echo "Code linting finished"
echo "Code linting finished" >> $RESULTS_FILE

echo "You can always check the results in '$RESULTS_FILE' file."
echo "Results: "
cat "$RESULTS_FILE" | more
