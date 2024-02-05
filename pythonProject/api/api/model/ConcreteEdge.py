from api.api.model.abstract.Edge import Edge
from api.api.model.abstract.Node import Node


class ConcreteEdge(Edge):
    def __init__(self, node1: Node, node2: Node):
        super(ConcreteEdge, self).__init__(node1=node1, node2=node2)
