import pkg_resources
from django.apps import AppConfig


class D3PlatformConfig(AppConfig):
    name = 'd3_platform'
    plugini_ucitavanje = []
    graph = None
    def ready(self):
        # Prilikom startovanja aplikacije, ucitavamo plugine na
        # vec poznati nacin.
        self.plugini_ucitavanje = load_plugins("graph.load")
        self.graph=None

def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins