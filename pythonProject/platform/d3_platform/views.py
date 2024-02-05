from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    plugini = apps.get_app_config('d3_platform').plugini_ucitavanje
    return render(request, "index.html", {"title": "Index", "plugini_ucitavanje": plugini})


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
