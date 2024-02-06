import abc


class DataSourceService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def name(self):
        pass
    @abc.abstractmethod
    def parse(self, path):
        pass