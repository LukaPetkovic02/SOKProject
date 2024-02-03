import json
import uuid


class JSONGraphDataSource:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def parse_json(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data

    def generate_graph(self, data):
        graph = {}
        node_ids = {}
        self._traverse(data, graph, node_ids)
        return graph

    def _traverse(self, obj, graph, node_ids, parent_id=None):
        if isinstance(obj, list):
            # Handle list objects separately
            for item in obj:
                self._traverse(item, graph, node_ids, parent_id=parent_id)
            return  # Stop processing further for this object

        if isinstance(obj, dict):
            obj_id = obj.get('@id')  # Get the value of @id field as the node ID
            if obj_id is None:
                obj_id = str(uuid.uuid4())  # Generate unique ID for the node
            graph[obj_id] = obj
            node_ids[id(obj)] = obj_id  # Use object's ID as key

            if parent_id:
                # If parent exists, add an edge from parent to current node
                if isinstance(graph[parent_id], dict):
                    graph[parent_id].setdefault('children', []).append(obj_id)

            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    self._traverse(value, graph, node_ids, parent_id=obj_id)


if __name__ == "__main__":
    json_file_path = "../resources/example.json"
    json_data_source = JSONGraphDataSource(json_file_path)
    json_data = json_data_source.parse_json()
    graph = json_data_source.generate_graph(json_data)

    formatted_graph = {}
    for node_id, node_data in graph.items():
        children = node_data.get("children", [])
        formatted_children = [child for child in children if isinstance(child, dict)]
        node_data["children"] = formatted_children
        formatted_graph[node_id] = node_data

    formatted_graph_json = json.dumps(formatted_graph, indent=4)
    print(formatted_graph_json)
