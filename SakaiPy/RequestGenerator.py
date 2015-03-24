#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import requests


baseURL=""
loginURL="/direct/session?_username={0}&_password={1}"

session = requests.Session()

class RequestGenerator(object):
    """This class handles the login/cookie mechanisms and request generation."""

    def __init__(self, connectionInfo):
        """Simply generate the session cookie"""

        self.baseURL=connectionInfo['baseURL']

        #Generate a session cookie & store it in the requesting session
        session.post(self.baseURL+loginURL.format(connectionInfo['username'],connectionInfo['password']))

    def executeRequest(self, url):
        """Returns the JSON response from the specified URL."""

        response = session.get(self.baseURL+url)

        """If it is a good response, then return the content in json form for the Sakai Object.
           If it is a bad response, raise an exception.
        """
        if response.status_code == 200:
            return (response.json())
        else:
            response.raise_for_status()





            