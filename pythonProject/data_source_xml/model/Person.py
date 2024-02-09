from api.model.abstract.Node import Node


class Person(Node):
    def __init__(self, **kwargs):
        super(Person, self).__init__(**kwargs)
        # self._data = kwargs.get("data", None)
        self._age = kwargs.get("age", None)
        self._children = kwargs.get("children", None)

    def get_data(self):
        data_dict = {}
        data_dict["age"] = self._age
        data_dict["children"] = self._children
        return data_dict
