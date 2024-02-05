from setuptools import setup, find_packages

setup(
    name="d3_platform",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=2.1'],
    package_data={'d3_platform':['static/*.css', 'static/*.js', 'static/*.html', 'templates/*.html']},
    zip_safe=False
)