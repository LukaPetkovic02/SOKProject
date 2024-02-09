from api.model.abstract.Node import Node


class Account(Node):
    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)
        # self._data = kwargs.get("data", None)
        self._email = kwargs.get("email", None)
        self._password = kwargs.get("password", None)
        self._phone = kwargs.get("phone", None)
        self._children = kwargs.get("children", None)

    def get_data(self):
        data_dict = {}
        data_dict["email"] = self._email
        data_dict["password"] = self._password
        data_dict["phone"] = self._phone
        data_dict["children"] = self._children
        return data_dict
