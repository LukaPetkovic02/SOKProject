from api.api.model.abstract.Node import Node


class ConcreteNode(Node):
    def __init__(self, **kwargs):
        super(ConcreteNode, self).__init__(**kwargs)
        self._data = kwargs.get("data", None)

    def get_data(self):
        return self._data