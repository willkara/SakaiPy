#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator


class Gradebook(object):

    def __init__(self, rq):
        self.requester = rq

    def getGradebookForSite(self, siteid):
        return self.requester.executeRequest('/direct/gradebook/site/{0}.json'.format(siteid))

    def getAllMyGrades(self):
        return self.requester.executeRequest('/direct/gradebook/my.json')

    def getGradeDetails(self, siteid, name):
        return self.requester.executeRequest('/direct/gradebook/event/{0}/{1}.json'.format(siteid,name))



