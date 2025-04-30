from mcp.server.fastmcp import FastMCP
from tg_client import TigerGraphClient
from config import HOST, GRAPH, SECRET

tg_client = TigerGraphClient(HOST, GRAPH, SECRET)
mcp = FastMCP("TigerGraphMCP")

@mcp.tool()
def get_schema():
    """MCP tool: Get TigerGraph schema."""
    return tg_client.get_schema()

@mcp.tool()
def run_query(query_name: str, params: dict = None):
    """MCP tool: Run a TigerGraph query with parameters."""
    return tg_client.run_query(query_name, params)

@mcp.tool()
def show_query(query_name: str):
    """MCP tool: Show the content of a GSQL query."""
    return tg_client.show_query(query_name)

@mcp.tool()
def get_installed_query():
    """MCP tool: List all installed GSQL queries."""
    return tg_client.get_installed_queries()

@mcp.tool()
def upsert_vertex(vertex_type: str, vertex_id: str, attributes: dict):
    """MCP tool: Insert or update a vertex."""
    return tg_client.upsert_vertex(vertex_type, vertex_id, attributes)

@mcp.tool()
def upsert_edge(source_type: str, source_id: str, edge_type: str,
                target_type: str, target_id: str, attributes: dict = None):
    """MCP tool: Insert or update an edge."""
    return tg_client.upsert_edge(source_type, source_id, edge_type, target_type, target_id, attributes)

@mcp.tool()
def get_vertex(vertex_type: str, vertex_id: str):
    """MCP tool: Retrieve a vertex by type and ID."""
    return tg_client.get_vertex(vertex_type, vertex_id)

@mcp.tool()
def run_gsql(query: str):
    """MCP tool: Run a raw GSQL query."""
    return tg_client.run_gsql(query)

@mcp.tool()
def list_all_algorithm(category: str = None):
    """MCP tool: List available built-in algorithms."""
    return tg_client.list_all_algorithms(category)

@mcp.tool()
def get_udf(ExprFunctions: bool = True, ExprUtil: bool = True, json_out=False):
    """MCP tool: Get UDF files."""
    return tg_client.get_udfs(ExprFunctions, ExprUtil, json_out)
