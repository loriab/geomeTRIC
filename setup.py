from setuptools import setup

setup(name='geometric',
      description='Geometry optimization for quantum chemistry',
      url='https://github.com/leeping/geomeTRIC',
      author='Lee-Ping Wang, Chenchen Song',
      packages=['geometric'],
      entry_points={
          'console_scripts': [
              'geometric-optimize = geometric.optimize:main',
          ]
      }
      )
