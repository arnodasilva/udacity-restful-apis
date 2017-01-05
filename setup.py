from setuptools import find_packages, setup

setup(
    name="meetneat",
    version="1.0.0",
    author="Arno Da Silva",
    author_email="arnodslv@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    # url="http://pypi.python.org/pypi/MyApplication_v010/",
    # license="",
    # description="",
    # long_description=open("README.txt").read(),
    install_requires=[
        "flask",
        "flask_inputs",
        "flask_restful",
        "jsonschema",
        "sqlalchemy",
    ],
)
