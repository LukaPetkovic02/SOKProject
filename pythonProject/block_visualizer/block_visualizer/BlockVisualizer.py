from api.model.Graph import Graph
from api.model.abstract.Node import Node
from api.model.abstract.Edge import Edge
from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
from uuid import uuid4

from api.model.ConcreteNode import ConcreteNode

from api.model.ConcreteEdge import ConcreteEdge


class BlockVisualizer:


    def visualizeGraph(self):
        p = Path(__file__).parent/"templates" # sample relative path
        print(p)

        g=Graph(True)
        n1=ConcreteNode(name="aa")
        n2=ConcreteNode(name="bb")
        e1=ConcreteEdge(n1,n2)

        g.add_node(n1)
        g.add_node(n2)
        g.add_edge(e1)

        print(p)
        templateLoader = FileSystemLoader(searchpath=p)
        templateEnv = Environment(loader=templateLoader)
        TEMPLATE_FILE = "block-directed.jinja"

        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(graph_nodes=g.nodes, graph_edges=g.edges)

        print(outputText)
        return outputText

