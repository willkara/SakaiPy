#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession
from SakaiPy import SakaiTools


class SakaiPy(object):
    """
    The main entry point for the program. Use this class to access all of the other tools.
    """

    def __init__(self, connectioninfo):
        """
        Create the main SakaiPy object. This object will be the main interface point.
        :param connectioninfo: A dict containing all of the needed information to create a session.
        """

        self.session = SakaiSession.SakaiSession(connectioninfo['username'], connectioninfo['password'],
                                                 connectioninfo['baseurl'])

    def get_calendar(self):
        """
        Get a calendar object
        :return:
        """
        return SakaiTools.Calendar.Calendar(self.session)

    def get_announcement(self):
        """
        Get an Announcements object
        :return:
        """
        return SakaiTools.Announcement.Announcement(self.session)

    def get_assignment(self):
        """
        Get an Assignments object
        :return:
        """
        return SakaiTools.Assignment.Assignment(self.session)

    def get_forums(self):
        """
        Get a forums object
        :return:
        """
        return SakaiTools.Forums.Forums(self.session)

    def get_gradebook(self):
        pass

    def get_workspace(self):
        """
        Get a MyWorkspace object
        :return:
        """
        return SakaiTools.MyWorkspace.MyWorkspace(self.session)

    def get_news(self):
        """
        Get a news object
        :return:
        """
        return SakaiTools.News.News(self.session)

    def get_webcontent(self):
        """
        Get a web content object
        :return:
        """
        return SakaiTools.WebContent.WebContent(self.session)
