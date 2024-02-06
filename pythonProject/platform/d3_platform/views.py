from django.apps.registry import apps
from django.shortcuts import render, redirect

from .apps import D3PlatformConfig


def index(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    graph = D3PlatformConfig.graph
    if(graph==None):
        print("NE POSTOJI JOS")
    else:
        for node in graph.nodes.values():
            print(node)
    return render(request, "my_template.html", {"plugini_ucitavanje": plugini,
                                                "graph":graph})


def ucitavanje_plugin(request, id):
    # Cuvanje identifikatora plugina na nivou sesije.
    request.session['izabran_plugin_ucitavanje'] = id
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    graph = D3PlatformConfig.graph
    # Trazimo plugin sa prosledjenim identifikatorom,
    for i in plugini:
        print(i.name())
        if i.name() == id:
            # te pozivamo funkciju koja podatke upisuje u bazu.
            if(id=="JSON"):
                print("NASAO "+i.name())
                graph = i.parse("../resources/example.json")
                #print(graph)
            elif(id=="XML"):
                print("NASAO " + i.name())
                graph = i.parse("../resources/example.xml")
            #i.ucitati()
    D3PlatformConfig.graph = graph
    return redirect("/")
