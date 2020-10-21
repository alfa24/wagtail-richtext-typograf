import os
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='wagtail-richtext-typograf',
    version='0.1',
    description='Typograf for wagtail richtext field',
    long_description=readme(),
    packages=find_packages(),
    url='https://github.com/alfa24/wagtail-richtext-typograf.git',
    author='Aleksandr Falichev',
    include_package_data=True,
)
