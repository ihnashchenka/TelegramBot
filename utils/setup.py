from setuptools import setup

setup(
   name='utils',
   version='1.0',
   description='DB utils',
   author='Tatsiana Ihnashchenka',
   packages=['utils'],  #same as name
   install_requires=[psycopg2], #external packages as dependencies
)