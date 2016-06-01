#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession


class Calendar(object):
    """
    Contains logic for the Sakai Calendar tool.

    More information about the RESTful interface can be found at:
    https://trunk-mysql.nightly.sakaiproject.org/direct/calendar/describe
    """

    def __init__(self, sess):
        """
        Create a standalone Calendar Object
        :param sess: The Session to use.
        :return: A Calendar object
        """
        assert isinstance(sess, SakaiSession.SakaiSession)
        self.session = sess

    def getAllMyEvents(self):
        """
        Get all of the currently available events for the currently logged in user.
        :return: A JSON representation of the currently available events for the currently logged in user.
        """
        return self.session.executeRequest('GET', '/calendar/my.json')

    def getEventDetails(self, siteid, eventid):
        """
        Get the details for the specified event within the specified site.
        :param siteid: The ID of the site.
        :param eventid: The ID of the event.
        :return: A JSON representation of the specified event within the specified site.
        """
        return self.session.executeRequest('GET', '/calendar/event/{0}/{1}.json'.format(siteid, eventid))
