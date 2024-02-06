import os

from django.apps.registry import apps
from django.shortcuts import render, redirect

from .apps import D3PlatformConfig


def index(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    plugins_visualizers=apps.get_app_config('d3_platform').visualizer_plugins
    graph = D3PlatformConfig.graph
    str=""
    if(graph==None):
        print("NE POSTOJI JOS")
    else:
        str=plugins_visualizers[0].visualizeGraph(graph)
    return render(request, "my_template.html", {"plugini_ucitavanje": plugini,"graph":graph,"graph_view":str})


def ucitavanje_plugin(request, file_name):
    # Cuvanje identifikatora plugina na nivou sesije.
    _, file_extension = os.path.splitext(file_name)
    file_extension = file_extension[1:]

    request.session['izabran_plugin_ucitavanje'] = file_extension
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    graph = D3PlatformConfig.graph
    # Trazimo plugin sa prosledjenim identifikatorom,
    for i in plugini:
        if i.name() == file_extension.upper():
            # te pozivamo funkciju koja podatke upisuje u bazu.
            if(file_extension.upper()=="JSON"):
                print("NASAO "+i.name())
                graph = i.parse("../resources/" + file_name)
                #print(graph)
            elif(file_extension.upper()=="XML"):
                print("NASAO " + i.name())
                graph = i.parse("../resources/" + file_name)
            #i.ucitati()
    D3PlatformConfig.graph = graph
    return redirect("/")
