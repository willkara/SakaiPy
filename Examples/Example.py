#!/usr/bin/python
# -*- coding: utf-8 -*-
import RequestGenerator
from SakaiTools import Announcement

"""Say I want to get a list of all of the announcements I have for a specific site. I'll write all the code first then explain each part."""

authInfo={}
authInfo['loginURL']="https://cas.rutgers.edu/login?service=https%3A%2F%2Fsakai.rutgers.edu%2Fsakai-login-tool%2Fcontainer"
authInfo['username']="Sheppppurd"
authInfo['password']="hunter2"

rq = RequestGenerator.RequestGenerator(authInfo)

announcements= Announcment.Announcment(rq).getAllForSite("ede5e4b7-9cf2-4eea-8dd4-276f244ed4c1")
print announcements["announcement_collection"]