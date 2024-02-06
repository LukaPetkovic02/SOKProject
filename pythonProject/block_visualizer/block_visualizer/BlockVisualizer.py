from api.model.Graph import Graph
from api.model.abstract.Node import Node
from api.model.abstract.Edge import Edge
from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
from uuid import uuid4

from api.model.ConcreteNode import ConcreteNode

from api.model.ConcreteEdge import ConcreteEdge


class BlockVisualizer:


    def visualizeGraph(self,graph:Graph):
        p = Path(__file__).parent/"templates" # sample relative path

        print(p)
        templateLoader = FileSystemLoader(searchpath=p)
        templateEnv = Environment(loader=templateLoader)

        if(graph.directed):
            TEMPLATE_FILE = "block-directed.jinja"
        else:TEMPLATE_FILE = "block.jinja"



        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(graph_nodes=graph.nodes, graph_edges=graph.edges)

        print(outputText)
        return outputText


