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
        for edge in graph.edges.values():
            if edge.node1.id == node1.id and edge.node2.id == node2.id:
                return False
            if not self._directed and edge.node1.id == node2.id and edge.node2.id == node1.id:
                return False
        return True



# ovo je samo primer kako se implementira klasa Node i Edge
# class ConcreteNode(Node):
#     def __init__(self, **kwargs):
#         super(ConcreteNode, self).__init__(**kwargs)
#         self._data = kwargs.get("data", None)
#
#     def get_data(self):
#         return self._data
#
# class ConcreteEdge(Edge):
#     def __init__(self, node1: Node, node2: Node):
#         super(ConcreteEdge, self).__init__(node1=node1, node2=node2)


graph = Graph(False)

# concrete_node = ConcreteNode(name="My Node")
# print("node1: ")
# print(concrete_node.to_json())
#
# concrete_node2 = ConcreteNode(name="My Node 2")
# print("node2: ")
# print(concrete_node2.to_json())
#
# concrete_edge = ConcreteEdge(node1=concrete_node, node2=concrete_node2)
# print("edge1: ")
# print(concrete_edge.to_json())
#
# concrete_edge2 = ConcreteEdge(node1=concrete_node2, node2=concrete_node)
# print("edge2: ")
# print(concrete_edge2.to_json())
#
#
# print(graph.add_edge(concrete_edge))
# print(graph.add_node(concrete_node))
# print(graph.add_node(concrete_node2))
# print(graph.add_edge(concrete_edge))
# print(graph.add_edge(concrete_edge))
# print(graph.add_edge(concrete_edge2))
#
# for edge in graph.edges.values():
#     print(edge.to_json())
#
# for node in graph.nodes.values():
#     print(node.to_json())
