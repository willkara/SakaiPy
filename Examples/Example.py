#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import RequestGenerator
from SakaiTools import Calendar

"""Say I want to get a list of all of the Calendars I have for a specific site. I'll write all the code first then explain each part."""

authInfo={}
authInfo['baseURL']="https://sakai.rutgers.edu"
authInfo['loginURL']="https://cas.rutgers.edu/login?service=https%3A%2F%2Fsakai.rutgers.edu%2Fsakai-login-tool%2Fcontainer"
authInfo['username']="Shepppppurd"
authInfo['password']="Bosh'tet"

rq = RequestGenerator.RequestGenerator(authInfo)

Calendars= Calendar.Calendar(rq).getAllMyEvents()
print Calendars["calendar_collection"]