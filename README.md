SakaiPy
=======

A library to access the information located on Sakai installations.

SakaiPy used to only work with Python 2.7, though now it works with Python 2.5> & Python 3.x. I have now re-wrote it so that it no longer has a dependency on the mechanize library which did not work on Python 3 yet. 

I'm mainly a Java developer so anyone with more Python experience is more than welcome to make a pull request to clean it up!

I made this library so people can access the Sakai information at their schools (I'm @ Rutgers) more easily through Python.

You can install SakaiPy with pip by typing in the following command:

```
pip install SakaiPy
```

I'll usually make a blog post about each new version at my website. http://willkara.com

### TO-DO
* Add events to Google Calendar
* Add more Sakai tools and more functionality for each tool.
* Better HTTP Code error handling- If something breaks return a code.

### Example


A quick example of its usage can be seen below. Here, I am create a dict() that contains some of the neccasary auth info and pass that to an instance of import SakaiPy.RequestGenerator which handles the actual requests. Depending on the tool you'll be using you then create an instance of that tool, pass the Request Generator and then use the method you wish.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import RequestGenerator
from SakaiPy.SakaiTools import Calendar

"""Say I want to get a list of all of the Calendars I have for a specific site. I'll write all the code first then explain each part."""

authInfo={}
authInfo['baseURL']="https://sakai.rutgers.edu"

authInfo['username']="Shepppppurd"
authInfo['password']="Bosh'tet"

rq = RequestGenerator.RequestGenerator(authInfo)

#Get all of your events within Calendar.
Calendars= Calendar.Calendar(rq).getAllMyEvents()
print Calendars["calendar_collection"]
```

* **authInfo** A dict containing some of the neccasary information to login to your Sakai system.

* **baseURL**  The FQDN of your school's Sakai installation.

* **username** Your username.
* **password** Your password.

* import SakaiPy.RequestGenerator is the class that handles the authentication and REST requests.

* You would then define an instance of the tool you wish to use and execute the query.

As of now, it returns to you the JSON representation of the data.

### Sakai Documentation

**ALL** of the data,endpoints and documentation can be found @ <<Sakai Installation URL>>/direct/describe. 



BTW: In no way,shape,form or Universe does Rutgers University endorse or have anything to do with this library. I made it myself. This library also does not speak for the Sakai Community Project either.
