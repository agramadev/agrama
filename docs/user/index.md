# User Guide

This guide provides instructions on how to use Agrama's Terminal User Interface (TUI) and interact with the system.

## Getting Started

After [installing Agrama](../installation.md), you can launch the TUI with:

```bash
agrama tui
```

## TUI Layout

The Agrama TUI is organized into several panels:

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

### Graph Tree

The Graph Tree panel displays the hierarchical structure of your knowledge graph. You can navigate through the tree using the arrow keys.

### Preview

The Preview panel shows the content of the selected node, which can be markdown text, code snippets, or other structured data.

### Neighbors

The Neighbors panel displays the edges (connections) from the currently selected node, along with their weights.

### Command Palette

The Command Palette allows you to enter commands to perform various actions, such as searching or time-traveling.

## Keyboard Shortcuts

Agrama's TUI uses keyboard shortcuts inspired by lazygit for navigation and actions:

| Key       | Action            |
| --------- | ----------------- |
| `→` / `←` | Traverse edge     |
| `↑` / `↓` | Navigate tree     |
| `s`       | Semantic search   |
| `/`       | Keyword search    |
| `t`       | Time-travel input |
| `p`       | Command palette   |
| `q`       | Quit              |

## Common Tasks

### Navigating the Graph

1. Use the arrow keys (`↑`, `↓`, `→`, `←`) to navigate through the graph tree
2. Press `→` to expand a node and see its children
3. Press `←` to collapse a node and go back to its parent

### Searching

#### Semantic Search

1. Press `s` to open the semantic search input
2. Enter your search query
3. Press Enter to execute the search
4. Navigate through the results using arrow keys

#### Keyword Search

1. Press `/` to open the keyword search input
2. Enter your search terms
3. Press Enter to execute the search
4. Navigate through the results using arrow keys

### Time Travel

To view a node at a specific point in time:

1. Select the node in the Graph Tree
2. Press `t` to open the time travel input
3. Enter a timestamp (in Unix milliseconds) or a relative time (e.g., "1h ago")
4. Press Enter to view the node at that time

### Using the Command Palette

1. Press `p` to open the command palette
2. Start typing a command
3. Use arrow keys to select from the suggestions
4. Press Enter to execute the selected command

## Example Workflows

### Exploring a Session

1. Launch the TUI with `agrama tui`
2. Navigate to a Session node in the Graph Tree
3. Press `→` to expand and see Tasks under that Session
4. Select a Task to view its details in the Preview panel
5. Check the Neighbors panel to see related nodes

### Finding Information

1. Press `s` for semantic search
2. Enter a natural language query like "TypeScript debounce implementation"
3. Navigate through the results
4. Press `→` on a result to explore related nodes

## Customization

You can customize the TUI appearance by modifying the `tui.tcss` file. The TUI supports both light and dark themes, which can be toggled with the `action_toggle_dark` command.
