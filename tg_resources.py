from tg_tools import mcp, get_vertex, run_query

@mcp.resource("tgraph://vertex/{vertex_type}/{vertex_id}")
def vertex_resource(vertex_type: str, vertex_id: str):
    """MCP resource: Vertex URI access."""
    return get_vertex(vertex_type, vertex_id)

@mcp.resource("tgraph://query/{query_name}/{params}")
def query_resource(query_name: str, params: dict = None):
    """MCP resource: Query URI access."""
    return run_query(query_name, params)
