#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession


class Assignment(object):
    """
    Contains logic for the Sakai Assignments tool.

    More information about the RESTful interface can be found at:
    https://trunk-mysql.nightly.sakaiproject.org/direct/assignment/describe
    """

    def __init__(self, sess):
        """
        Create a standalone Assignment Object.
        :param sess: The Session to use.
        :return: An Assignment object.
        """
        assert isinstance(sess, SakaiSession.SakaiSession)
        self.session = sess

    def getAllMyAssignments(self):
        """
        Get ALL of the assignments for the currently logged in user.
        :return: A JSON representation of all of the assignments for the currently logged in user.
        """
        return self.session.executeRequest('GET', '/assignment/my.json')

    def getAssignmentInfo(self, assignmentid):
        """
        Get information for a given assignment.
        :param assignmentid: The ID of the assignment.
        :return: A JSON representation of the information for the given Assignment.
        """
        return self.session.executeRequest('GET', '/assignment/item/{0}.json'.format(assignmentid))
