#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator


class Calendar(object):

    def __init__(self, rq):
        self.requester = rq

    def getCalendarForSite(self, siteid):
        return self.requester.executeRequest('/direct/calendar/site/{0}.json'.format(siteid))

    def getAllMyEvents(self):
        return self.requester.executeRequest('/direct/calendar/my.json')

    def getEventDetails(self, siteid, eventid):
        return self.requester.executeRequest('/direct/calendar/event/{0}/{1}.json'.format(siteid,eventid))



