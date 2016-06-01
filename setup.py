#!/usr/bin/env python

from setuptools import setup

setup(name='SakaiPy',
      version='2.2.1',
      description='Python interface to the Sakai RESTful API\'s',
      license='MIT',
      author='William Karavites',
      author_email='wkaravites@gmail.com',
      url='https://github.com/willkara/SakaiPy',
      download_url = 'https://github.com/willkara/SakaiPy/archive/2.2.1.tar.gz',
      packages=['SakaiPy', 'SakaiPy.SakaiTools'],
      install_requires=['requests'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Education',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'
      ],
      keywords='Sakai Education RESTful API'
      )
