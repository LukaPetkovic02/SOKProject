from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    plugins_visualizers=apps.get_app_config('d3_platform').visualizer_plugins
    grap=plugini[0].parse("/Users/borislavcelar/Documents/GitHub/SOKProject/pythonProject/resources/example.json")
    str=plugins_visualizers[0].visualizeGraph(grap)
    return render(request, "my_template.html", {"plugini_ucitavanje": plugini,"graph_view":str})


def ucitavanje_plugin(request, id):
    # Cuvanje identifikatora plugina na nivou sesije.
    request.session['izabran_plugin_ucitavanje'] = id
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    # Trazimo plugin sa prosledjenim identifikatorom,
    for i in plugini:
        if i.identifier() == id:
            # te pozivamo funkciju koja podatke upisuje u bazu.
            i.ucitati()
    return redirect('index')
