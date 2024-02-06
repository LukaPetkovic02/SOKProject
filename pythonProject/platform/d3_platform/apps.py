import pkg_resources
from django.apps import AppConfig


class D3PlatformConfig(AppConfig):
    name = 'd3_platform'
    plugini_ucitavanje = []
    visualizer_plugins=[]

    def ready(self):
        # Prilikom startovanja aplikacije, ucitavamo plugine na
        # vec poznati nacin.
        self.plugini_ucitavanje = load_plugins("graph.load")
        self.visualizer_plugins=load_plugins("graph.visualize")


def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins