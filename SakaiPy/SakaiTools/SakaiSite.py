#!/usr/bin/python
# -*- coding: utf-8 -*-



class SakaiSite(object):
    """
    The representation of a Sakai Site. This class handles most of/ if not all of the site specific functions.
    Use this class to  get information for a specific Sakai Site.
    """

    def __init__(self, rq, siteid):
        """
        Create a SakaiSite object for the given siteid. This object can handle all of the operations available for the given site.
        :param rq: The RequestHandler to use for this SakaiSite object
        :param siteid: The id of the site you wish you get.
        :return: A SakaiSite object
        """
        self.requester = rq
        self.siteid = siteid

    def getMemership(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/membership/site/{0}.json'.format(self.siteid))

    def getRoster(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/roster/site/{0}.json'.format(self.siteid))

    def getGradebook(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/gradebook/site/{0}.json'.format(self.siteid))

    def getNews(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/news/site/{0}.json'.format(self.siteid))

    def getCalendar(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/calendar/site/{0}.json'.format(self.siteid))

    def getAnnouncements(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/announcement/site/{0}.json'.format(self.siteid))

    def getForums(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/forums/site/{0}.json'.format(self.siteid))

    def getContents(self):
        """
        Get the membership for the given site.
        :return: A JSON reprentation of the membership of the given site.
        """
        return self.requester.executeRequest('/direct/content/site/{0}.json'.format(self.siteid))
