from setuptools import setup, find_packages

setup(
    name="api",
    version="0.1",
    packages=find_packages(),
    #namespace_packages=['api', 'api.model', 'api.model.abstract', 'api.service'],
    zip_safe=True
)