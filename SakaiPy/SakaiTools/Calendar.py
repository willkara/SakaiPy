#!/usr/bin/python
# -*- coding: utf-8 -*-


class Calendar(object):
    """
    Contains logic for the Sakai Calendar tool.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/direct/calendar/describe
    """
    def __init__(self, rq):
        """
        Create a standalone Calendar Object
        :param rq: The RequestHandler to use.
        :return: A Calendar object
        """
        self.requester = rq

    def getAllMyEvents(self):
        """
        Get all of the currently available events for the currently logged in user.
        :return: A JSON representation of the currently available events for the currently logged in user.
        """
        return self.requester.executeRequest('/direct/calendar/my.json')

    def getEventDetails(self, siteid, eventid):
        """
        Get the details for the specified event within the specified site.
        :param siteid: The ID of the site.
        :param eventid: The ID of the event.
        :return: A JSON representation of the specified event within the specified site.
        """
        return self.requester.executeRequest('/direct/calendar/event/{0}/{1}.json'.format(siteid, eventid))
