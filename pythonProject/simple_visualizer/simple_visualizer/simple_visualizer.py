from api.model.abstract.Visualizer import Visualizer
from api.model.Graph import Graph
from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path

# (Visualizer)
class SimpleVisualizer(Visualizer):

    def __str__(self):
        return 'SimpleVisualizer'

    def visualizeGraph(self, graph:Graph):
        p = Path(__file__).parent / "templates"

        templateLoader = FileSystemLoader(searchpath=p)
        templateEnv = Environment(loader=templateLoader)

        if (graph.directed):
            TEMPLATE_FILE = "simple-directed.jinja"
        else:
            TEMPLATE_FILE = "simple.jinja"

        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(graph_nodes=graph.nodes, graph_edges=graph.edges)

        return outputText