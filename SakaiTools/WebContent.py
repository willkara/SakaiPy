#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class WebContent(object):

    def __init__(self, rq):
        self.requester = rq


    def getWebContentForSite(self,siteid):
        return self.requester.executeRequest('/direct/webcontent/site/{0}.json'.format(siteid))
