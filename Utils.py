#!/usr/bin/python
# -*- coding: utf-8 -*-

def createDirs(path):
	try: 
	    os.makedirs(path)
	except OSError:
	    if not os.path.isdir(path):
	        raise