#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

try:
    license = open('LICENSE').read()
except:
    license = None

try:
    readme = open('README.rst').read()
except:
    readme = None

setup(
    name='TornadIO',
    version='0.0.5',
    author='Hiveary',
    author_email='info@hiveary.com',
    packages=['tornadio'],
    scripts=[],
    url='http://github.com/hiveary/tornadio/',
    license=license,
    description='Socket.io server implementation on top of Tornado framework',
    long_description=readme,
    requires=['simplejson', 'tornado'],
    install_requires=[
        'simplejson >= 2.1.0',
        'tornado >= 3.1.1'
    ]
)
