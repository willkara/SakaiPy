#!/usr/bin/python
# -*- coding: utf-8 -*-


class News(object):
    """
    Contains logic for the Sakai News tool.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/direct/news/describe
    """
    def __init__(self, rq):
        """
        Create a standalone News Object
        :param rq: The RequestHandler to use.
        :return: A News object
        """
        self.requester = rq

    def getNewsForSite(self, siteid):
        """
        Get the News object for the specified site.
        :param siteid: The ID of the site.
        :return: A JSON representation of the News object for the given site.
        """
        return self.requester.executeRequest('/direct/news/site/{0}.json'.format(siteid))
