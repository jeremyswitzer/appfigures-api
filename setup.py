from setuptools import setup, find_packages
'''The setup and build script for the appfigures library.'''

__author__ = 'jeremy.switzer@gmail.com'
__version__ = '0.1dev'

setup(
  name = "appfigures",
  version = __version__,
  author='Jeremy Switzer',
  author_email=__author__,
  description='A Python wrapper around the AppFigures API',
  license='MIT',
  url='https://github.com/trezorg/podio-py.git',
  keywords='podio',
  packages= find_packages(),
  install_requires = ['requests'],
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2 :: Only'
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet',
  ],
)
