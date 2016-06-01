#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession


class MyWorkspace(object):
    """
    Contains logic for the Sakai Content (Resources) tool.
    Works with Site Content and My Workspace Content.

    More information about the RESTful interface can be found at:
    https://trunk-mysql.nightly.sakaiproject.org/direct/content/describe
    """

    def __init__(self, sess):
        """
        Create a standalone Content Object
        :param sess: The Session to use.
        :return: A Content object
        """
        assert isinstance(sess, SakaiSession.SakaiSession)
        self.session = sess

    def getMyWorkspaceContent(self):
        """
        Get the My Workspace content for the currently logged in user.
        :return: A JSON representation of the My Workspace content for the currently logged in user.
        """
        return self.session.executeRequest('GET', '/calendar/my.json')
