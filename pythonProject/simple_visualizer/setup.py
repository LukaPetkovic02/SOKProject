from setuptools import setup, find_packages

setup(
    name="graph-visualizer-simple",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-platform>=0.1'],
    entry_points = {
        'graph.visualize':
            ['graph_visualizer_simple=simple_visualizer.simple_visualizer:SimpleVisualizer'],
    },
    zip_safe=True
)