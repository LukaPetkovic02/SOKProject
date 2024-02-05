from django.apps.registry import apps
from django.shortcuts import render

from api.model.ConcreteEdge import ConcreteEdge
from api.model.ConcreteNode import ConcreteNode
from api.model.Graph import Graph


def force_layout(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    graphs = Graph.objects.all()
    nodes = ConcreteNode.objects.all()
    edges = ConcreteEdge.objects.all()
    return render(request, "forceLayout.html",
                  {"title": "Force layout",
                   "plugini_ucitavanje": plugini,
                   "graphs": graphs,
                   "nodes": nodes,
                   "edges":edges
                   })

def tree_layout(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    graphs = Graph.objects.all()
    nodes = ConcreteNode.objects.all()
    edges = ConcreteEdge.objects.all()
    return render(request, "treeLayout.html",
                  {"title": "Tree layout",
                   "plugini_ucitavanje": plugini,
                   "graphs": graphs,
                   "nodes": nodes,
                   "edges": edges
                   })