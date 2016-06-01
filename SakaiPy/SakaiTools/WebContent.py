#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession


class WebContent(object):
    """
    Contains logic for the Sakai WebContent tool.

    More information about the RESTful interface can be found at:
    https://trunk-mysql.nightly.sakaiproject.org/webcontent/news/describe
    """

    def __init__(self, sess):
        """
        Create a standalone WebContent Object
        :param sess: The Session to use.
        :return: A WebContent object
        """
        assert isinstance(sess, SakaiSession.SakaiSession)
        self.session = sess

    def getWebContentForSite(self, siteid):
        """
        YOU GET A WEBCONTENT, YOU GET A WEBCONTENT, EVERYONE GETS A WEBCONTENT!
        :param siteid: The siteid you wish to use.
        :return: Webcontent information for the specified site.
        """
        return self.requester.executeRequest('GET', '/webcontent/site/{0}.json'.format(siteid))
