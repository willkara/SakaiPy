#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class Assignment(object):

    def __init__(self, rq):
        self.requester = rq

    def getAllAssignmentsForSite(self, siteid):
        return self.requester.executeRequest('/direct/assignment/site/{0}.json'.format(siteid))

    def getAllMyAssignments(self):
        return self.requester.executeRequest('/direct/assignment/my.json')

    def getAssignmentInfo(self, assignment_id):
        return self.requester.executeRequest('/direct/assignment/item/{0}.json'.format(assignment_id))



