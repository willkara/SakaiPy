#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class News(object):

    def __init__(self, rq):
        self.requester = rq

    def getNewsForSite(self, siteid):
        return self.requester.executeRequest('/direct/news/site/{0}.json'.format(siteid))



			