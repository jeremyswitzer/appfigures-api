from setuptools import setup, find_packages
'''The setup and build script for the appfigures library.'''

__author__ = 'jeremy.switzer@gmail.com'
__version__ = '1.0RC'

setup(
  name = "appfigures",
  version = __version__,
  author='Jeremy Switzer',
  author_email=__author__,
  description='A Python wrapper around the AppFigures API',
  license='MIT',
  url='https://github.com/jeremyswitzer/appfigures-api',
  keywords='appfigures',
  packages= find_packages(),
  install_requires = ['requests'],
  tests_require = ['mock'],
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2 :: Only'
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet',
  ],
)
