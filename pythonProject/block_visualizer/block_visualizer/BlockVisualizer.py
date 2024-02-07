from api.model.abstract.Visualizer import Visualizer
from api.model.Graph import Graph
from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path


class BlockVisualizer(Visualizer):


    def visualizeGraph(self,graph:Graph):
        p = Path(__file__).parent/"templates" # sample relative path

        templateLoader = FileSystemLoader(searchpath=p)
        templateEnv = Environment(loader=templateLoader)

        if(graph.directed):
            TEMPLATE_FILE = "block-directed.jinja"
        else:TEMPLATE_FILE = "block.jinja"



        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(graph_nodes=graph.nodes, graph_edges=graph.edges)

        return outputText
