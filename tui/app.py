"""
Agrama TUI - Textual UI for Agrama
"""

from textual.app import App
from textual.widgets import Header, Footer, Tree
from textual.containers import Horizontal, Vertical


class AgramaTUI(App):
    """Agrama TUI application."""

    CSS_PATH = "tui.tcss"
    BINDINGS = [
        ("s", "semantic_search", "Semantic Search"),
        ("/", "keyword_search", "Keyword Search"),
        ("t", "time_travel", "At Time"),
        ("p", "command_palette", "Command Palette"),
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        """Compose the app layout."""
        yield Header()

        # Create the tree widget
        self.tree = Tree("Memory")
        self.tree.root.expand()

        # Create the neighbors widget (placeholder)
        self.neighbors = Vertical(id="neighbors")

        # Create the preview widget (placeholder)
        self.preview = Vertical(id="preview")

        # Create the command palette (placeholder)
        self.command_palette = Vertical(id="command-palette")

        # Compose the layout
        yield Horizontal(
            Vertical(self.tree, id="graph-tree"),
            Vertical(
                self.preview,
                self.neighbors,
                self.command_palette,
            ),
        )

        yield Footer()

    def action_semantic_search(self):
        """Handle semantic search action."""
        self.notify("Semantic search not implemented yet")

    def action_keyword_search(self):
        """Handle keyword search action."""
        self.notify("Keyword search not implemented yet")

    def action_time_travel(self):
        """Handle time travel action."""
        self.notify("Time travel not implemented yet")

    def action_command_palette(self):
        """Handle command palette action."""
        self.notify("Command palette not implemented yet")


if __name__ == "__main__":
    app = AgramaTUI()
    app.run()
