from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # Kada korisnik pogodi ovaj endpoint (http://127.0.0.1:8000/ucitavanje/plugin/ucitati_prodavnice_kod),
    # doci ce do ucitavanja plugina, ciji je identifikator "ucitati_prodavnice_kod".
    path('ucitavanje/plugin/<str:file_name>', views.ucitavanje_plugin, name="ucitavanje_plugin"),
    path('ucitavanje/visualizer/<str:selectedOption>', views.ucitavanje_visualizer, name="ucitavanje_visualizer"),
    path('search/<str:input>',views.search, name="search"),
    path('filter', views.filter, name="filter_data"),
    path('reset',views.reset, name="reset"),
    # path('primer1', views.primer1, name="primer1"),
    # path('primer2', views.primer2, name="primer2"),
    # path('primer3', views.primer3, name="primer3"),
    #
    # path('primer4', views.primer4, name="primer4"),

    # path('primer/pan/zoom', views.primerPanZoom, name="primerPanZoom"),
]