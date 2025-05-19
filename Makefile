.PHONY: dev seed test bench load proto docs setup clean lint venv

# Start development containers
dev:
	docker compose up -d

# Load sample data
seed:
	@echo "Loading sample data..."
	python -m agrama.scripts.seed_data

# Run tests
test:
	pytest

# Run tests with coverage
test-cov:
	pytest --cov=agrama --cov-report=term --cov-report=html

# Run benchmarks
bench:
	pytest --benchmark-autosave
	pytest-benchmark compare --sort=mean

# Run load tests with k6
load:
	@./scripts/run-k6-tests.sh

# Generate protocol buffers
proto:
	@echo "Generating protocol buffers..."
	@./scripts/generate_proto.sh

# Build documentation
docs:
	mkdocs build

# Serve documentation locally
docs-serve:
	mkdocs serve

# Setup development environment
setup:
	pip install -r requirements.txt
	pip install -e .

# Create virtual environment
venv:
	python -m venv .venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source .venv/bin/activate (Linux/macOS)"
	@echo "  .venv\\Scripts\\activate (Windows)"

# Run linting
lint:
	ruff check .
	black --check .
	mypy agrama

# Format code
format:
	ruff check --fix .
	black .

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +

# Help command
help:
	@echo "Agrama Makefile commands:"
	@echo "  make dev         - Start development containers"
	@echo "  make seed        - Load sample data"
	@echo "  make test        - Run tests"
	@echo "  make test-cov    - Run tests with coverage"
	@echo "  make bench       - Run benchmarks"
	@echo "  make load        - Run load tests with k6"
	@echo "  make proto       - Generate protocol buffers"
	@echo "  make docs        - Build documentation"
	@echo "  make docs-serve  - Serve documentation locally"
	@echo "  make setup       - Setup development environment"
	@echo "  make venv        - Create virtual environment"
	@echo "  make lint        - Run linting tools"
	@echo "  make format      - Format code"
	@echo "  make clean       - Clean build artifacts"
