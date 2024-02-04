import abc


class DataSourceService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse(self, path):
        pass