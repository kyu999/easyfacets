#!/usr/bin/env python

from setuptools import find_packages, setup


description = ''
REQUIRED_PACKAGES = [
    'ipython==6.5.0',
    'numpy==1.16.2',
    'pandas==0.23.4',
    'seaborn==0.9.0'
]

setup(name='easyfacets',
      version='0.1',
      license='MIT',
      description=description,
      long_description=description,
      author="kyu999",
      author_email="kyukokkyou999@gmail.com",
      maintainer="kyu999",
      maintainer_email="kyukokkyou999@gmail.com",
      url='https://github.com/kyu999/easyfacets',
      packages=find_packages(),
      install_requires=REQUIRED_PACKAGES,
      )