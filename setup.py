'''
setup.py for wal
'''
from setuptools import setup, find_packages
import os


setup(
    name = 'wal',
    version = '0.1',
    description = 'web automation layer',
    long_description = (
        'a browser automation tool with a yaml front end '
        'and selenium/python/phantomjs bacd end'),
    author = 'Kolby',
    author_email = 'kolby@fasterdevops.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
	'Operating System :: POSIX',
	'Operating System :: POSIX :: Linux',
	'Operating System :: Unix',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
	'Topic :: Internet'],
    keywords = 'web automation layer',
    install_requires = [
        'PyYAML==3.12',
        'selenium==2.53.2',
        'simplejson==3.10.0',
        'six==1.10.0',
        'urllib3==1.15.1']
    home-page: 'https://fasterdevops.github.io/'
    download-url = 'https://github.com/classmember/wal/archive/master.zip'
    requires-python >= '3.4'
)