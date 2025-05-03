# TG_MCP
![Integration](https://github.com/user-attachments/assets/cea6c4a3-1293-4bac-8c20-d1ecd7f0e866)


A lightweight Python interface that exposes TigerGraph operations (queries, schema, vertices, edges, UDFs) as structured tools and URI-based resources for MCP agents.

## Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Installation](#installation)  
4. [Configuration](#configuration)  
5. [Connecting to Claude](#connecting-to-claude)
6. [Examples](#examples)  
7. [Contributing](#contributing)  
8. [License](#license)  

## Features

- **Schema Introspection**  
  Retrieve full graph schema (vertex & edge types).

- **Query Execution**  
  Run installed GSQL queries or raw GSQL strings with parameters.

- **Vertex & Edge Upsert**  
  Create or update vertices and edges programmatically.

- **Resource URIs**  
  Access graph objects through `tgraph://vertex/...` and `tgraph://query/...` URIs.

- **UDF & Algorithm Listing**  
  Fetch installed user-defined functions and GDS algorithm catalogs.

## Project Structure

```
TG_MCP/
├── config.py            # Environment config (HOST, GRAPH, SECRET)
├── tg_client.py         # Encapsulates TigerGraphConnection and core operations
├── tg_tools.py          # `@mcp.tool` definitions exposing client methods
├── tg_resources.py      # `@mcp.resource` URI handlers
├── main.py              # MCP app bootstrap (`mcp.run()`)
├── pyproject.toml       # Project metadata & dependencies
├── LICENSE              # MIT License
└── .gitignore           # OS/Python ignore rules
```

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Muzain187/TG_MCP.git
   cd TG_MCP
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install .
   ```
   > Requires `mcp[cli]>=1.6.0` and `pyTigerGraph>=1.8.6`.

## Configuration

Set the following environment variables before running:

```bash
export TG_HOST=https://<your-tigergraph-host>
export TG_GRAPH=<your-graph-name>
export TG_SECRET=<your-api-secret>
```

These are read by `config.py`.


## Connecting to Claude

This MCP server can be installed into the **Claude Desktop** client so that Claude can invoke your TigerGraph tools directly:

```bash
uv run mcp install main.py
```

After running the above, restart Claude Desktop and you’ll see your MCP tools available via the hammer 🛠 icon.

## Examples:
![image](https://github.com/user-attachments/assets/3ba65cc2-8e24-45d5-8f12-c4b76739fb39)

![image](https://github.com/user-attachments/assets/032b85b9-4021-438e-9380-1ac96ae6c601)


## Contributing

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes  
   ```bash
   git commit -m "Add YourFeature"
   ```
4. Push to branch  
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request  

Please ensure all new code is covered by tests and follows PEP-8 style.

## License

This project is licensed under the **MIT License**.  
