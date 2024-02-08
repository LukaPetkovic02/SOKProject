from api.model.abstract.Edge import Edge
from api.model.abstract.Node import Node


class Graph:
    def __init__(self, value: bool):
        # super(Graph, self).__init__()
        self._nodes = {}
        self._edges = {}
        self._directed = value

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value: dict):
        self._nodes = value

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, value: dict):
        self._edges = value

    @property
    def directed(self):
        return self._directed

    @directed.setter
    def directed(self, value: bool):
        self._directed = value

    def add_nodes(self, value: list):
        for node in value:
            self.add_node(node)

    def add_node(self, node: Node):
        if node.id not in self._nodes:
            self._nodes[node.id] = node
            return True
        else:
            return False
    def add_edges(self, value: list):
        for edge in value:
            self.add_edge(edge)

    def add_edge(self, edge: Edge):
        if edge.node1.id not in self._nodes or edge.node2.id not in self._nodes:
            return False

        if not self.valid_edge(edge.node1, edge.node2):
            return False


        if edge.id not in self._edges:
            self._edges[edge.id] = edge
            return True

        return False

    def valid_edge(self, node1: Node, node2: Node) -> bool:
        for edge in self.edges.values():
            if edge.node1.id == node1.id and edge.node2.id == node2.id:
                return False
            if not self._directed and edge.node1.id == node2.id and edge.node2.id == node1.id:
                return False
        return True

    def serialize(self):
        serialized_nodes = [node.to_json() for node_id, node in self.nodes.items()]
        serialized_edges = [edge.to_json() for edge_id, edge in self.edges.items()]

        return {
            "nodes": serialized_nodes,
            "edges": serialized_edges,
            "directed": self.directed
        }
