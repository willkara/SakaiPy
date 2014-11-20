#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class Announcement(object):

    def __init__(self, rq):
        self.requester = rq

    def getAllForSite(self, siteid):
        return self.requester.executeRequest('/direct/announcement/site/{0}.json'.format(siteid))

