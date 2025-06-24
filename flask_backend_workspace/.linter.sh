#!/bin/bash
cd /home/kavia/workspace/code-generation/dailyquotekeeper-67253-3ff53e54/flask_backend_workspace/flask_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

