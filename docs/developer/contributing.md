# Contributing Guide

Thank you for your interest in contributing to Agrama! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/agrama.git
   cd agrama
   ```
3. Set up your development environment as described in the [Developer Guide](index.md)
4. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

Agrama follows a test-driven development approach:

1. Create a functional specification in a `SPEC.md` file within the feature folder
2. Write automated tests covering the desired behavior
3. Implement code to satisfy the tests

### Coding Standards

- Follow PEP 8 style guide for Python code
- Use type hints for function parameters and return values
- Write docstrings for all functions, classes, and modules
- Keep functions small and focused on a single responsibility
- Use meaningful variable and function names

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality. Install them with:

```bash
pre-commit install
```

The pre-commit hooks will run automatically when you commit changes.

## Testing

All code changes should include appropriate tests:

- Unit tests for individual functions and classes
- Integration tests for component interactions
- Property-based tests for data model invariants
- Performance tests for critical paths

Run the tests with:

```bash
make test
```

## Pull Request Process

1. Update the documentation to reflect any changes
2. Run all tests and ensure they pass
3. Update the changelog with your changes
4. Submit a pull request to the `main` branch
5. Address any feedback from code reviewers

### Pull Request Template

When creating a pull request, please include:

- A clear and descriptive title
- A detailed description of the changes
- Any related issues (e.g., "Fixes #123")
- Screenshots or examples if applicable
- Checklist of completed items

## Release Process

Agrama follows semantic versioning:

- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backward-compatible manner
- PATCH version for backward-compatible bug fixes

The release process is managed by the core team.

## Documentation

All new features should include appropriate documentation:

- Update the relevant sections in the `/docs` folder
- Add examples and usage instructions
- Document any configuration options
- Update API documentation for new endpoints

## Getting Help

If you need help with contributing to Agrama, you can:

- Open an issue on GitHub
- Reach out to the maintainers
- Check the existing documentation

Thank you for contributing to Agrama!
