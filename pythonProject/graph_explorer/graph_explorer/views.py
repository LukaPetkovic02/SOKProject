# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Welcome to my Django site!")
from django.shortcuts import render
from django.apps.registry import apps
import pkg_resources



def my_view(request):

    for ep in pkg_resources.iter_entry_points(group='graph.visualize'):
        o=ep.load()
        print(o)
        operator=o()
        str=operator.visualizeGraph()
        print(operator)
        context = {
            'graph_view': str,
        }
        return render(request, 'my_template.html',context)

