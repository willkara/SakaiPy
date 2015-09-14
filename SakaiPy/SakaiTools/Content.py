#!/usr/bin/python
# -*- coding: utf-8 -*-


class Content(object):
    """
    Contains logic for the Sakai Content (Resources) tool.
    Works with Site Content and My Workspace Content.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/direct/content/describe
    """
    def __init__(self, rq):
        """
        Create a standalone Content Object
        :param rq: The RequestHandler to use.
        :return: A Content object
        """
        self.requester = rq

    def getMyWorkspaceContent(self):
        """
        Get the My Workspace content for the currently logged in user.
        :return: A JSON representation of the My Workspace content for the currently logged in user.
        """
        return self.requester.executeRequest('/direct/calendar/my.json')
