import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

setup(
    name='RecipeGenerator',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/avivamunshi/RecipeGenerator',
    license='MIT',
    author='RecipeGenerator',
    author_email='avivamunshi@gmail.com',
    description='Recipe Generator App',
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
    ],
)
