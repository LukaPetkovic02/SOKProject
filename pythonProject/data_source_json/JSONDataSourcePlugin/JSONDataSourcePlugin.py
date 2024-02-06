import json

from api.model.ConcreteEdge import ConcreteEdge
from api.model.ConcreteNode import ConcreteNode
from api.service.DataSourceService import DataSourceService

from api.model.Graph import Graph


class JSONDataSourcePlugin(DataSourceService):
    def name(self):
        return("JSON")

    def parse(self, json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            graph = Graph(True)  # Pravimo usmeren graf

            # Kreiramo cvorove i dodajemo ih u graf
            nodes = {}
            for node_data in data:
                node_id = node_data['id']
                node_name = node_data['name']
                node_data_dict={}
                node_data_dict['age'] = node_data['age']
                node = ConcreteNode(name=node_name, data=node_data_dict)
                nodes[node_id] = node
                graph.add_node(node)

            for node_data in data:
                node_id = node_data['id']
                children_ids = node_data['children']
                for child_id in children_ids:
                    edge = ConcreteEdge(nodes[node_id], nodes[child_id])
                    graph.add_edge(edge)

            return graph

#
# if __name__ == "__main__": # ovo mozete zakomentarisati ako vam bude smetalo
#     json_file_path = "../resources/example.json"
#     graph = parse_json_to_graph(json_file_path)
#
#     print("Directed graph")
#     print("Nodes:")
#     for node in graph.nodes.values():
#         print(node)
#
#     print("\nEdges:")
#     for edge in graph.edges.values():
#         print(edge)
