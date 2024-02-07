from abc import ABC, abstractmethod

from api.model.Graph import Graph


class Visualizer(ABC):
    @abstractmethod
    def visualizeGraph(self, graph:Graph):
        pass
