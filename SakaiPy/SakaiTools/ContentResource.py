#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class ContentResource(object):

    def __init__(self, rq):
        self.requester = rq

    def getContentsForSite(self, siteid):
        return self.requester.executeRequest('/direct/content/site/{0}.json'.format(siteid))

    def getMyWorkspaceContent(self):
        return self.requester.executeRequest('/direct/calendar/my.json'.format(siteid))


        



			