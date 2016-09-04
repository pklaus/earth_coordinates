
from setuptools import setup

setup(name='earth_coordinates',
      version='0.1',
      description='A package to help parsing human input of coordinates (latitude & longitude)',
      url='https://github.com/pklaus/earth_coordinates',
      author='Philipp Klaus',
      author_email='philipp.l.klaus@web.de',
      license='MIT',
      packages=['earth_coordinates', 'earth_coordinates.scripts'],
      entry_points = {
          'console_scripts': [
              'interpret_coordinates_cli = earth_coordinates.scripts.interpret_coordinates_cli:main',
          ],
      },
      zip_safe=False)
