# TUI Implementation Specification

## Overview

This document specifies the Terminal User Interface (TUI) for Agrama, which provides an interactive way to explore and manipulate the knowledge graph. The TUI is built using the Textual library and follows a layout similar to lazygit, with a focus on keyboard-driven navigation and a clean, intuitive interface.

## Screen Layout

```
┌──────── Graph Tree ────────┐┌─ Preview ────────┐
│ Session › Task › …         ││ Markdown / code  │
│ (Keyboard: ↑ ↓ → ←)        │└──────────────────┘
├──────── Neighbors ─────────┤
│ Edge list w/ weights       │
├──────── Command Palette ───┤
│ > _                        │
└────────────────────────────┘
```

The layout consists of the following components:

1. **Graph Tree**: A tree widget showing the hierarchical structure of the knowledge graph.
2. **Preview**: A pane showing the content of the selected node, rendered as markdown or code.
3. **Neighbors**: A list of neighboring nodes connected by edges to the selected node.
4. **Command Palette**: A command input area for executing commands.

## Keyboard Navigation

The TUI uses keyboard shortcuts inspired by lazygit for navigation:

| Key       | Action            |
| --------- | ----------------- |
| `→` / `←` | Traverse edge     |
| `↑` / `↓` | Navigate tree     |
| `s`       | Semantic search   |
| `/`       | Keyword search    |
| `t`       | Time-travel input |
| `p`       | Command palette   |
| `q`       | Quit              |

## Component Implementation

### Graph Tree

The Graph Tree is implemented using Textual's `Tree` widget:

```python
class GraphTree(Tree):
    def __init__(self, label="Memory"):
        super().__init__(label)
        self.root.expand()

    def load_graph(self, root_uuid):
        # Clear the tree
        self.root.remove_children()

        # Load the root node
        node = get_node(root_uuid)
        if not node:
            return

        # Add the root node to the tree
        root_item = self.root.add(node.uuid, expand=True)
        root_item.data = node

        # Load the children
        self._load_children(root_item, node.uuid)

    def _load_children(self, parent_item, parent_uuid):
        # Get the children
        edges = get_edges(parent_uuid, "contains", "out")

        # Add the children to the tree
        for edge in edges:
            node = get_node(edge.dst)
            if not node:
                continue

            # Add the child to the tree
            child_item = parent_item.add(node.uuid)
            child_item.data = node
```

### Preview Pane

The Preview Pane is implemented using Textual's `Markdown` widget:

```python
class Preview(Markdown):
    def update_content(self, node):
        if not node:
            self.update("")
            return

        # Get the content
        content = node.content.decode("utf-8", errors="ignore")

        # Update the markdown
        self.update(content)
```

### Neighbors List

The Neighbors List is implemented using Textual's `ListView` widget:

```python
class Neighbors(ListView):
    def update_neighbors(self, uuid):
        # Clear the list
        self.clear()

        # Get the neighbors
        edges = get_edges(uuid, None, "out")

        # Add the neighbors to the list
        for edge in edges:
            node = get_node(edge.dst)
            if not node:
                continue

            # Add the neighbor to the list
            self.append(ListItem(f"{edge.type}: {node.uuid}"))
```

### Command Palette

The Command Palette is implemented using Textual's `Input` widget:

```python
class CommandPalette(Input):
    def on_input_submitted(self, event):
        # Get the command
        command = event.value

        # Clear the input
        self.value = ""

        # Execute the command
        self.execute_command(command)

    def execute_command(self, command):
        # Parse the command
        parts = command.split()
        if not parts:
            return

        # Execute the command
        if parts[0] == "search":
            self.app.action_semantic_search(parts[1:])
        elif parts[0] == "goto":
            self.app.goto_node(parts[1])
        # ... other commands
```

## Main Application

The main application is implemented as a Textual `App`:

```python
class AgramaTUI(App):
    CSS_PATH = "tui.tcss"
    BINDINGS = [
        ("s", "semantic_search", "Semantic Search"),
        ("/", "keyword_search", "Keyword Search"),
        ("t", "time_travel", "At Time"),
        ("p", "command_palette", "Command Palette"),
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        yield Header()

        # Create the tree widget
        self.tree = GraphTree("Memory")

        # Create the neighbors widget
        self.neighbors = Neighbors()

        # Create the preview widget
        self.preview = Preview()

        # Create the command palette
        self.command_palette = CommandPalette()

        # Compose the layout
        yield Horizontal(
            Vertical(self.tree, id="graph-tree"),
            Vertical(
                self.preview,
                self.neighbors,
                self.command_palette,
            )
        )

        yield Footer()
```

## CSS Styling

The TUI is styled using Textual's CSS-like styling system:

```css
/* Main layout */
#graph-tree {
    width: 30%;
    min-width: 30;
    border: solid green;
}

#preview {
    height: 50%;
    border: solid blue;
}

#neighbors {
    height: 30%;
    border: solid red;
}

#command-palette {
    height: 20%;
    border: solid yellow;
}

/* Dark mode */
.dark {
    background: $surface-darken-1;
    color: $text;
}

/* Light mode */
.light {
    background: $surface-lighten-1;
    color: $text;
}
```

## Theme Toggle

The TUI supports toggling between dark and light themes:

```python
def action_toggle_dark(self):
    """Toggle between dark and light mode."""
    self.dark = not self.dark
```

## API Integration

The TUI integrates with the Agrama API to fetch and manipulate data:

```python
async def get_node(uuid):
    """Get a node from the API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/nodes/{uuid}")
        if response.status_code != 200:
            return None
        return response.json()

async def get_edges(uuid, edge_type=None, direction="out"):
    """Get edges from the API."""
    params = {}
    if edge_type:
        params["edge_type"] = edge_type
    params["direction"] = direction

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/edges/{uuid}", params=params)
        if response.status_code != 200:
            return []
        return response.json()["edges"]
```

## Future Enhancements

- Add support for editing nodes and edges
- Implement a history feature for navigation
- Add support for visualizing the graph as a network
- Implement a search results view
- Add support for multiple tabs
