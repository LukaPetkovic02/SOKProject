from api.model.abstract.Node import Node


class Person(Node):
    def __init__(self, **kwargs):
        super(Person, self).__init__(**kwargs)
        # self._data = kwargs.get("data", None)
        self._age = kwargs.get("age", None)
        self._lastName = kwargs.get("lastName", None)
        self._email = kwargs.get("email", None)

    def get_data(self):
        data_dict = {}
        data_dict["age"] = self._age
        data_dict["lastName"] = self._lastName
        data_dict["email"] = self._email
        return data_dict
