import xml.etree.ElementTree as ET
from api.model.Graph import Graph
from model.Account import Account
from model.AccountEdge import AccountEdge
from api.service.DataSourceService import DataSourceService


class XMLDataSourcePlugin(DataSourceService):
    def name(self):
        return("XML")

    def parse(self, xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        data = root.findall('entity')
        graph = Graph(False)  # Pravimo neusmeren graf

        # Kreiramo cvorove i dodajemo ih u graf
        nodes = {}
        for node_data in data:
            node_id = node_data.get('id')
            node_name = node_data.get('name')

            children = []
            for child in node_data.findall('children/child'):
                children.append(child.get('ref'))

            node = Account(name=node_name, email=node_data.get('email'), password=node_data.get('password'), phone=node_data.get('phone'), children=children)
            nodes[node_id] = node
            graph.add_node(node)

        for node_data in data:
            node_id = node_data.get('id')
            children = node_data.find('children')
            if children is not None:
                for child in children.findall('child'):
                    child_id = child.get('ref')
                    edge = AccountEdge(nodes[node_id], nodes[child_id])
                    graph.add_edge(edge)
        return graph