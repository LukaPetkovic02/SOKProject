from abc import ABC, abstractmethod


class Visualizer(ABC):
    @abstractmethod
    def generate_graph(self, graph):
        pass

    @abstractmethod
    def generate_directed_graph(self, graph):
        pass

    @abstractmethod
    def generate_undirected_graph(self, graph):
        pass
