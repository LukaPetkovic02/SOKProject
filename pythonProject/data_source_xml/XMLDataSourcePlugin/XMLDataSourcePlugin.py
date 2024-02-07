import xml.etree.ElementTree as ET
from api.model.Graph import Graph
from api.model.ConcreteEdge import ConcreteEdge
from api.model.ConcreteNode import ConcreteNode
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
            node_data_dict = {}
            node_data_dict['age'] = int(node_data.get('age'))
            node = ConcreteNode(name=node_name, data=node_data_dict)
            nodes[node_id] = node
            graph.add_node(node)

        for node_data in data:
            node_id = node_data.get('id')
            children = node_data.find('children')
            if children is not None:
                for child in children.findall('child'):
                    child_id = child.get('ref')
                    edge = ConcreteEdge(nodes[node_id], nodes[child_id])
                    graph.add_edge(edge)

        return graph

# if __name__ == "__main__": # ovo mozete zakomentarisati ako vam bude smetalo
#     xml_file_path = "../resources/example.xml"
#     graph = parse_xml_to_graph(xml_file_path)
#
#     print("Undirected graph")
#     print("Nodes:")
#     for node in graph.nodes.values():
#         print(node)
# 
#     print("\nEdges:")
#     for edge in graph.edges.values():
#         print(edge)