#!/usr/bin/python
# -*- coding: utf-8 -*-


class WebContent(object):
    """
    Contains logic for the Sakai WebContent tool.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/webcontent/news/describe
    """

    def __init__(self, rq):
        """
        Create a standalone WebContent Object
        :param rq: The RequestHandler to use.
        :return: A WebContent object
        """
        self.requester = rq

    def getWebContentForSite(self, siteid):
        """
        YOU GET A WEBCONTENT, YOU GET A WEBCONTENT, EVERYONE GETS A WEBCONTENT!
        :param siteid: PIZZA!
        :return: HOTDOGS!
        """
        return self.requester.executeRequest('/direct/webcontent/site/{0}.json'.format(siteid))
