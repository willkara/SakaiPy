#!/usr/bin/python
# -*- coding: utf-8 -*-

baseUrl = ""


class RequestHandler(object):
    """
    This class handles all of the RESTful web commands and execution.
    """

    def __init__(self, session, url):
        """
        Create and save the RequestHandler object. This object handles all of the POST/GET and other HTTP method functions.
        :param session: The request.session() object you wish to use.
        :param url: The base URL of your Sakai instance.
        :return: A RequestHandler object to execute HTTP RESTful methods
        """
        self.baseURL = url
        self.session = session

    """This class handles the login/cookie mechanisms and request generation."""

    def executeRequest(self, url):
        """
        Execute a GET request to the specified URL.
        :param url: The URL to GET
        :return: A JSON representation of the GET response.
        """

        """Returns the JSON response from the specified URL."""
        response = self.session.get(self.baseURL + url)

        """If it is a good response, then return the content in json form for the Sakai Object.
           If it is a bad response, raise an exception.
        """
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
