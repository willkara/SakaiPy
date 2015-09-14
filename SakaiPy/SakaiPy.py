#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from SakaiPy import RequestHandler
from SakaiPy.SakaiTools import SakaiSite, Announcement, Assignment, Calendar, Content, Forums, Gradebook, News

loginURL = "/direct/session?_username={0}&_password={1}"

session = requests.Session()


class SakaiPy(object):
    """
    The main entry point for the program. Use this class to access all of the other tools.
    """

    def __init__(self, connectioninfo):
        """
        Create the main SakaiPy object. All logic for the program flows through this object
        :param connectioninfo: A dict containin the connection/credential information neccsary to authenticate the user.
        :return: A SakaiPy object
        """

        """Generate the session cookie"""
        self.baseURL = connectioninfo['baseURL']

        # Generate a session cookie & store it in the requesting session
        session.post(self.baseURL + loginURL.format(
            connectioninfo['username'],
            connectioninfo['password']
        ))

        self.requester = RequestHandler.RequestHandler(session, self.baseURL)

    def getSakaiSite(self, siteid):
        """
        Generate and return a SakaiSite object
        :param siteid: The id of the site.
        :return: A SakaiSite object
        """
        return SakaiSite.SakaiSite(self.requester, siteid)

    def getAnnouncementObject(self):
        """
        Generate and return an Announcement object for the current user.
        :return: An announcement object for the currently logged in user.
        """
        return Announcement.Announcement(self.requester)

    def getAssignmentObject(self):
        """
        Generate and return an Assignment object for the current user.
        :return: An assignment object for the currently logged in user.
        """
        return Assignment.Assignment(self.requester)

    def getCalendarObject(self):
        """
        Generate and return a Calendar object for the current user.
        :return: A calendar object for the currently logged in user.
        """
        return Calendar.Calendar(self.requester)

    def getContentObject(self):
        """
        Generate and return a Content object for the current user.
        :return: A content object for the currently logged in user.
        """
        return Content.Content(self.requester)

    def getForumsObject(self):
        """
        Generate and return a Forums object for the current user.
        :return: A Forums object for the currently logged in user.
        """
        return Forums.Forums(self.requester)

    def getGradebookObject(self):
        """
        Generate and return a Gradebook object for the current user.
        :return: A Gradebook object for the currently logged in user.
        """
        return Gradebook.Gradebook(self.requester)

    def getNewsObject(self):
        """
        Generate and return a News object for the current user.
        :return: A News object for the currently logged in user.
        """
        return News.News(self.requester)
