from setuptools import setup, find_packages

setup(
    name="graph-visualize-block",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-platform>=0.1'],
    entry_points = {
        'graph.visualize':
            ['graph_visualize_block=block_visualizer.BlockVisualizer:BlockVisualizer'],
    },
    include_package_data=True,  # Include package data specified in MANIFEST.in
    package_data={
        '': ['templates/*'],  # Include all files under the 'data' directory
    },
    zip_safe=True
)