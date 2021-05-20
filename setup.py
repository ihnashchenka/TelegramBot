from setuptools import setup

setup(
   name='utils',
   version='1.0',
   description='DB utils',
   author='Tatsiana Ihnashchenka',
   packages=['utils'],  #same as name
   install_requires=[psycopg2], #external packages as dependencies
)

setup(
   name='objects',
   version='1.0',
   description='Represents object from db',
   author='Tatsiana Ihnashchenka',
   packages=['objects'],  #same as name
   install_requires=[], #external packages as dependencies
)