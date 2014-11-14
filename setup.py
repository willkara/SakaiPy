#!/usr/bin/env python

from distutils.core import setup

setup(name='SakaiPy',
      version='1.0',
      description='Python interface to the Sakai RESTful API\'s',
      license='MIT',
      author='William Karavites',
      author_email='wkaravites@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['SakaiTools'],
      requires={
      		"mechanize",
      		"cookielib",
      		"requests",
      		"simplejson",
                  "google-api-python-client"}
     )
			