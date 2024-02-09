from setuptools import setup, find_packages

setup(
    name="graph-visualize-simple",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-platform>=0.1'],
    entry_points = {
        'graph.visualize':
            ['graph_visualize_simple=simple_visualizer.simple_visualizer:SimpleVisualizer'],
    },
    include_package_data=True,
    package_data={
        '': ['templates/*'],
    },
    zip_safe=True
)