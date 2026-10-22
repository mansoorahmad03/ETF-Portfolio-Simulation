#!/bin/bash
# solve.sh - Executes the primary investment portfolio simulation pipeline
set -e

echo "Running production portfolio asset compilation engine..."
python3 /app/solution/solution.py
echo "Compilation complete."
