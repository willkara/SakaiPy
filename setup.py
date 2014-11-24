#!/usr/bin/env python

from distutils.core import setup

setup(name='SakaiPy',
      version='1.1.1',
      description='Python interface to the Sakai RESTful API\'s',
      license='MIT',
      author='William Karavites',
      author_email='wkaravites@gmail.com',
      url='https://github.com/willkara/SakaiPy',
      packages=['SakaiPy','SakaiPy.SakaiTools'],
      install_requires={
      		"mechanize",
      		"requests",
      		"simplejson"},
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
            'Programming Language :: Python :: 2.7'
      ],
      keywords='Sakai Education RESTful'
     )
			
