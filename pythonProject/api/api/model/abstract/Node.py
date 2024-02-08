from abc import ABC, abstractmethod
from uuid import uuid4


class Node(ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        super(Node, self).__init__()
        self._id = uuid4()
        self._name = kwargs.get("name", None)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "data": self.get_data()
        }

    @abstractmethod
    def get_data(self):
        pass

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._id == other.id
        return False


