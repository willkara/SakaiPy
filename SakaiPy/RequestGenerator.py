#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanize
import cookielib
import requests

try:
    import simplejson as json
except ImportError:
    import json

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()

baseURL=""


class RequestGenerator(object):
    """This class handles the login/cookie mechanisms and request generation."""

    # Browser

    br.set_cookiejar(cj)

    def __init__(self, connectionInfo):
        wPage = br.open(connectionInfo['loginURL'])
        self.baseURL=connectionInfo['baseURL']

        fCount=0

        for form in br.forms():
            if str(form.attrs["id"])==connectionInfo["loginFormId"]:
                break;
            fCount = fCount+1

        br.select_form(nr=fCount)

        br.form[connectionInfo['usernameField']] = connectionInfo['username']
        br.form[connectionInfo['passwordField']] = connectionInfo['password']

        br.submit()

    def executeRequest(self, url):
        """Returns the JSON response from the specified URL."""

        response = requests.get(self.baseURL+url, cookies=cj)

        """If it is a good response, then return the content in json form for the Sakai Object.
           If it is a bad response, raise an exception.
        """
        if response.status_code == 200:
            return (response.json())
        else:
            response.raise_for_status()





			