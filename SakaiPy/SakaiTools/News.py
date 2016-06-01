#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession


class News(object):
    """
    Contains logic for the Sakai News tool.

    More information about the RESTful interface can be found at:
    https://trunk-mysql.nightly.sakaiproject.org/direct/news/describe
    """

    def __init__(self, sess):
        """
        Create a standalone News Object
        :param sess: The Session to use.
        :return: A News object
        """
        assert isinstance(sess, SakaiSession.SakaiSession)
        self.session = sess

    def getNewsForSite(self, siteid):
        """
        Get the News object for the specified site.
        :param siteid: The ID of the site.
        :return: A JSON representation of the News object for the given site.
        """
        return self.session.executeRequest(self.session.baseurl, 'GET', '/news/site/{0}.json'.format(siteid))
