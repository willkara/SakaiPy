#!/usr/bin/python
# -*- coding: utf-8 -*-


class Assignment(object):
    """
    Contains logic for the Sakai Assignments tool.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/direct/assignment/describe
    """
    def __init__(self, rq):
        """
        Create a standalone Assignment Object.
        :param rq: The RequestHandler to use.
        :return: An Assignment object.
        """
        self.requester = rq

    def getAllMyAssignments(self):
        """
        Get ALL of the assignments for the currently logged in user.
        :return: A JSON representation of all of the assignments for the currently logged in user.
        """
        return self.requester.executeRequest('/direct/assignment/my.json')

    def getAssignmentInfo(self, assignmentid):
        """
        Get information for a given assignment.
        :param assignmentid: The ID of the assignment.
        :return: A JSON representation of the information for the given Assignment.
        """
        return self.requester.executeRequest('/direct/assignment/item/{0}.json'.format(assignmentid))
