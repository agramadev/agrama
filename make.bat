@echo off
setlocal enabledelayedexpansion

if "%1"=="" (
    echo Usage: make.bat [command]
    echo Available commands:
    echo   dev        - Start development containers
    echo   seed       - Load sample data
    echo   test       - Run tests
    echo   bench      - Run benchmarks
    echo   load       - Run k6 load tests
    echo   proto      - Generate protocol buffers
    echo   docs       - Build documentation
    echo   docs-serve - Serve documentation locally
    goto :eof
)

if "%1"=="dev" (
    echo Starting development containers...
    docker-compose up -d
    goto :eof
)

if "%1"=="seed" (
    echo Loading sample data...
    REM Add your seed command here
    goto :eof
)

if "%1"=="test" (
    echo Running tests...
    pytest
    goto :eof
)

if "%1"=="bench" (
    echo Running benchmarks...
    pytest --benchmark-autosave
    pytest-benchmark compare --sort=mean
    goto :eof
)

if "%1"=="load" (
    echo Running load tests...
    REM Add your k6 load test command here
    goto :eof
)

if "%1"=="proto" (
    echo Generating protocol buffers...
    REM Add your proto generation command here
    goto :eof
)

if "%1"=="docs" (
    echo Building documentation...
    mkdocs build
    goto :eof
)

if "%1"=="docs-serve" (
    echo Serving documentation locally...
    mkdocs serve
    goto :eof
)

echo Unknown command: %1
echo Run 'make.bat' without arguments to see available commands.
