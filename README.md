SakaiPy
=======

A library to access the information located on Sakai installations.

I made this library so people can access the Sakai information at their schools (I'm @ Rutgers).

It's finally up on PyPi so you can install it with:

```
pip install SakaiPy
```

### TO-DO
* Get the damn setup.py install script to work correctly.
* Have the ability to specify the login form id for mechanize.
* Add events to Google Calendar
* Finish adding tools

### Example

Once I get the setup.py script to work correctly you should be able to do:

from SakaiPy import SakaiPy, SakaiTools

A quick example of its usage can be seen below. Here, I am create a dict() that contains some of the neccasary auth info and pass that to an instance of import SakaiPy.RequestGenerator which handles the actual requests. Depending on the tool you'll be using you then create an instance of that tool, pass the Request Generator and then use the method you wish.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import RequestGenerator
from SakaiPy.SakaiTools import Calendar

"""Say I want to get a list of all of the Calendars I have for a specific site. I'll write all the code first then explain each part."""

authInfo={}
authInfo['baseURL']="https://sakai.rutgers.edu"
authInfo['loginURL']="https://cas.rutgers.edu/login?service=https%3A%2F%2Fsakai.rutgers.edu%2Fsakai-login-tool%2Fcontainer"
authInfo['username']="Shepppppurd"
authInfo['password']="Bosh'tet"

rq = RequestGenerator.RequestGenerator(authInfo)

Calendars= Calendar.Calendar(rq).getAllMyEvents()
print Calendars["calendar_collection"]
```

* authInfo is a dict containing the URL of the login page. This code will change to also take in the ID name of the login form.
* baseURL is the baseic FQDN of your school's Sakai installation
* Username is your username
* Password is your password

* import SakaiPy.RequestGenerator is the class that handles the authentication and REST requests.

* You would then define an instance of the tool you wish to use and execute the query.

As of now, it returns to you the JSON representation of the data.



BTW: In no way,shape,form or Universe does Rutgers University endorse or have anything to do with this library. I made it myself.
