#!/bin/bash
# Helper script for documentation tasks

# Ensure the script directory exists
mkdir -p scripts

# Make the script executable
chmod +x scripts/docs.sh

# Function to display help
show_help() {
    echo "Agrama Documentation Helper"
    echo ""
    echo "Usage: ./scripts/docs.sh [command]"
    echo ""
    echo "Commands:"
    echo "  serve      Start the documentation server (default)"
    echo "  build      Build the documentation site"
    echo "  deploy     Deploy the documentation to GitHub Pages"
    echo "  help       Show this help message"
    echo ""
}

# Function to serve the documentation
serve_docs() {
    echo "Starting documentation server..."
    mkdocs serve
}

# Function to build the documentation
build_docs() {
    echo "Building documentation..."
    mkdocs build
    echo "Documentation built in the 'site' directory."
}

# Function to deploy the documentation
deploy_docs() {
    echo "Deploying documentation to GitHub Pages..."
    mkdocs gh-deploy --force
    echo "Documentation deployed."
}

# Main script logic
case "$1" in
    serve|"")
        serve_docs
        ;;
    build)
        build_docs
        ;;
    deploy)
        deploy_docs
        ;;
    help)
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        show_help
        exit 1
        ;;
esac

exit 0
