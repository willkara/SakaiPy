#!/usr/bin/python
# -*- coding: utf-8 -*-


class Announcement(object):
    """
    Contains logic for the Sakai Announcement Tool.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/direct/announcement/describe
    """
    def __init__(self, rq):
        """
        Create a standalone Announcement Object
        :param rq: The RequestHandler to use.
        :return: An Announcement object
        """
        self.requester = rq

    def getAllAnnouncements(self, siteid):
        """
        Get all of the available announcements for a given site
        :param siteid: The id of the site you wish to get the announcements from
        :return: A JSON representation of the announcements for the given site.
        """
        return self.requester.executeRequest('/direct/announcement/site/{0}.json'.format(siteid))

    def getMessageOfTheDay(self):
        """
        Get the current Message Of The Day if there is one.
        :return: A JSON representation of the current Message Of The Day
        """
        return self.requester.executeRequest('/direct/announcement/motd.json')

    def getMyAnnouncements(self):
        """
        Get all of the current Announcements for the current user.
        :return: A JSON representation of all of the announcements for the current user.
        """
        return self.requester.executeRequest('/direct/announcement/user.json')
