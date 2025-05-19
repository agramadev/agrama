#!/usr/bin/env python3
"""
Agrama CLI - Command Line Interface for Agrama
"""

import argparse
import sys
from typing import List, Optional


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description="Agrama - A local micro-stack for knowledge management and retrieval"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # TUI command
    subparsers.add_parser("tui", help="Start the Textual UI")

    # API command
    api_parser = subparsers.add_parser("api", help="Start the API server")
    api_parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host to bind to"
    )
    api_parser.add_argument("--port", type=int, default=8000, help="Port to bind to")

    # Version command
    subparsers.add_parser("version", help="Show version information")

    parsed_args = parser.parse_args(args)

    if parsed_args.command == "tui":
        return run_tui()
    elif parsed_args.command == "api":
        return run_api(parsed_args.host, parsed_args.port)
    elif parsed_args.command == "version":
        return show_version()
    else:
        parser.print_help()
        return 0


def run_tui() -> int:
    """Run the Textual UI."""
    try:
        # This will be implemented later
        from tui.app import AgramaTUI

        app = AgramaTUI()
        app.run()
        return 0
    except ImportError:
        print("Error: Textual UI not available. Make sure textual is installed.")
        return 1


def run_api(host: str, port: int) -> int:
    """Run the API server."""
    try:
        import uvicorn

        print(f"Starting API server at http://{host}:{port}")
        uvicorn.run("agrama.api.main:app", host=host, port=port, reload=True)
        return 0
    except ImportError:
        print(
            "Error: API server not available. Make sure fastapi and uvicorn are installed."
        )
        return 1


def show_version() -> int:
    """Show version information."""
    from agrama import __version__

    print(f"Agrama version {__version__}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
