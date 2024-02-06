import os
import copy

from api.model.Graph import Graph
from django.apps.registry import apps
from django.shortcuts import render, redirect

from .apps import D3PlatformConfig


def index(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    plugins_visualizers=apps.get_app_config('d3_platform').visualizer_plugins
    graph = D3PlatformConfig.graph
    str=""
   # if(graph==None):
   #     print("NE POSTOJI JOS")
   # else:
   #     str=plugins_visualizers[0].visualizeGraph(graph)
   # return render(request, "my_template.html", {"plugini_ucitavanje": plugini,"graph":graph,"graph_view":str})
    whole_graph = D3PlatformConfig.whole_graph
    queries = D3PlatformConfig.queries
    if(graph==None):
        print("NE POSTOJI JOS")
    else:
        str=plugins_visualizers[0].visualizeGraph(graph)
        for node_id, node in graph.nodes.items():
            print(f"{node_id} {node.name} {node.get_data()}")

    print("WHOLEEE")
    if (whole_graph == None):
        print("NE POSTOJI JOS")
    else:
        for node_id, node in whole_graph.nodes.items():
            print(f"{node_id} {node.name} {node.get_data()}")
    return render(request, "my_template.html", {"plugini_ucitavanje": plugini,
                                                "graph":graph, "queries":queries, "graph_view":str})
def reset(request):
    whole_graph = D3PlatformConfig.whole_graph
    D3PlatformConfig.graph = whole_graph

    D3PlatformConfig.queries = []

    return redirect("/")


def search(request, input):
    graph = D3PlatformConfig.graph
    if graph is None:
        return redirect("/")

    filtered_nodes = {}
    filtered_edges = {}

    input_upper = input.upper()

    for node_id, node in graph.nodes.items():
        if input_upper in node.name.upper():
            filtered_nodes[node_id] = node
        else:
            node_data = node.get_data()
            if any(input_upper in str(value).upper() for value in node_data.values()):
                filtered_nodes[node_id] = node

    for edge_id, edge in graph.edges.items():
        if edge.node1.id in filtered_nodes and edge.node2.id in filtered_nodes:
            filtered_edges[edge_id] = edge

    filtered_graph = Graph(graph.directed)
    filtered_graph.nodes = filtered_nodes
    filtered_graph.edges = filtered_edges

    whole_graph_copy = copy.deepcopy(D3PlatformConfig.whole_graph)

    D3PlatformConfig.graph = filtered_graph

    D3PlatformConfig.whole_graph = whole_graph_copy

    queries = D3PlatformConfig.queries
    queries.append(input)
    return redirect("/")


def ucitavanje_plugin(request, file_name):
    _, file_extension = os.path.splitext(file_name)
    file_extension = file_extension[1:]

    request.session['izabran_plugin_ucitavanje'] = file_extension
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    graph = D3PlatformConfig.graph

    for i in plugini:
        if i.name() == file_extension.upper():
            if(file_extension.upper()=="JSON"):
                print("NASAO "+i.name())
                graph = i.parse("../resources/" + file_name)
            elif(file_extension.upper()=="XML"):
                print("NASAO " + i.name())
                graph = i.parse("../resources/" + file_name)
    D3PlatformConfig.graph = graph
    D3PlatformConfig.whole_graph = copy.deepcopy(graph)
    return redirect("/")
