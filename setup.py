#!/usr/bin/env python

from distutils.core import setup

setup(name='SakaiPy',
      version='1.0',
      description='Python interface to the Sakai RESTful API\'s',
      license='MIT',
      author='William Karavites',
      author_email='wkaravites@gmail.com',
      url='https://github.com/willkara/SakaiPy',
      packages=['SakaiPy','SakaiPy/SakaiTools'],
      requires={
      		"mechanize",
      		"cookielib",
      		"requests",
      		"simplejson"}
     )
			
