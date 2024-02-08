from api.model.abstract.Edge import Edge
from api.model.abstract.Node import Node


class PersonEdge(Edge):
    def __init__(self, node1: Node, node2: Node):
        super(PersonEdge, self).__init__(node1=node1, node2=node2)