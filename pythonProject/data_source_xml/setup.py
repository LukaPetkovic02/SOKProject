from setuptools import setup, find_packages

setup(
    name="graph-load-xml",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-platform>=0.1'],
    entry_points = {
        'graph.load':
            ['graph_load_xml=XMLDataSourcePlugin.XMLDataSourcePlugin:XMLDataSourcePlugin'],
    },
    zip_safe=True
)