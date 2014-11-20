#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class Roster(object):

    def __init__(self, rq):
        self.requester = rq

    def getSiteRoster(self, siteid):
        return self.requester.executeRequest('/direct/roster/site/{0}.json'.format(siteid))



			