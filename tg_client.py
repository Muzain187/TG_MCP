from pyTigerGraph import TigerGraphConnection
from typing import Dict, Tuple, Union
import pandas as pd

class TigerGraphClient:
    """Encapsulates all TigerGraph operations for MCP."""

    def __init__(self, host: str, graph: str, secret: str):
        self.conn = TigerGraphConnection(
            host=host,
            graphname=graph,
            gsqlSecret=secret
        )
        self.conn.apiToken = self.conn.getToken(secret)[0]

    def get_schema(self):
        return self.conn.getSchema()

    def run_query(self, query_name: str, params: dict = None):
        return self.conn.runInstalledQuery(query_name, params or {})

    def show_query(self, query_name: str):
        return self.conn.showQuery(query_name)

    def get_installed_queries(self):
        return self.conn.getInstalledQueries()

    def upsert_vertex(self, vertex_type: str, vertex_id: str, attributes: dict):
        return self.conn.upsertVertex(vertex_type, vertex_id, attributes)

    def upsert_edge(self, source_type: str, source_id: str, edge_type: str,
                    target_type: str, target_id: str, attributes: dict = None):
        return self.conn.upsertEdge(source_type, source_id, edge_type,
                                    target_type, target_id, attributes or {})

    def get_vertex(self, vertex_type: str, vertex_id: str):
        return self.conn.getVertexData(vertex_type, vertex_id)

    def run_gsql(self, query: str):
        return self.conn.gsql(query=query, graphname=self.conn.graphname)

    def list_all_algorithms(self, category: str = None):
        return self.conn.gds.featurizer().listAlgorithms(category)

    def get_udfs(self, ExprFunctions=True, ExprUtil=True, json_out=False):
        return self.conn.getUDF(ExprFunctions, ExprUtil, json_out)
