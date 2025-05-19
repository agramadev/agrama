#!/bin/bash
# Script to run k6 load tests for Agrama

# Ensure we're in the project root directory
cd "$(dirname "$0")/.." || exit

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
  echo "Error: Docker is not running or not installed."
  echo "Please start Docker and try again."
  exit 1
fi

# Function to run a k6 test
run_test() {
  local script=$1
  local name=$(basename "$script" .js)

  echo "Running $name test..."
  docker run --rm -i grafana/k6 run - < "$script"

  # Check exit status
  if [ $? -eq 0 ]; then
    echo "✅ $name test passed"
  else
    echo "❌ $name test failed"
    exit_code=1
  fi

  echo ""
}

# Initialize exit code
exit_code=0

# Check if specific test is requested
if [ $# -gt 0 ]; then
  if [ -f "$1" ]; then
    run_test "$1"
  else
    echo "Error: Test script '$1' not found."
    exit 1
  fi
else
  # Run basic test
  run_test "k6/script.js"

  # Ask if user wants to run advanced test
  read -p "Do you want to run the advanced test? (y/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    run_test "k6/advanced-script.js"
  fi
fi

exit $exit_code
