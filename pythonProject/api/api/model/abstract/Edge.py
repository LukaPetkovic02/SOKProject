from abc import ABC, abstractmethod
from uuid import uuid4

from api.model.abstract.Node import Node


class Edge(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        super(Edge, self).__init__()
        self._id = uuid4()
        self._node1 = kwargs.get("node1", None)
        self._node2 = kwargs.get("node2", None)

    @property
    def id(self):
        return self._id

    @property
    def node1(self):
        return self._node1

    @node1.setter
    def node1(self, value: Node):
        self._node1 = value

    @property
    def node2(self):
        return self._node2

    @node2.setter
    def node2(self, value: Node):
        self._node2 = value

    def to_json(self):
        return{
            "id": self.id,
            "node1": self.node1.id,
            "node2": self.node2.id
        }

    def __str__(self):
        return str(self.node1) + " - " + str(self.node2)

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self._id == other.id
        return False