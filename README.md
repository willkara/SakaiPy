SakaiPy
=======

A library to access the information located on Sakai installations.

SakaiPy currently only works with Python 2.x (2.7) since mechanize does not work on 3.x yet. If anyone knows of a 3.x tool that can take mechanizes place, please feel free to develop that feature.

I made this library so people can access the Sakai information at their schools (I'm @ Rutgers).

It's finally up on PyPi so you can install it with:

```
pip install SakaiPy
```

I'll usually make a blog post about each new version at my website. http://willkara.com

### TO-DO
* Add events to Google Calendar
* Finish adding tools
* HTTP Code error handling- If something breaks return a code.

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

authInfo['loginFormId']='fm1'
authInfo['usernameField']='username'
authInfo['passwordField']='password'

authInfo['loginURL']="https://cas.rutgers.edu/login?service=https%3A%2F%2Fsakai.rutgers.edu%2Fsakai-login-tool%2Fcontainer"
authInfo['username']="Shepppppurd"
authInfo['password']="Bosh'tet"

rq = RequestGenerator.RequestGenerator(authInfo)

Calendars= Calendar.Calendar(rq).getAllMyEvents()
print Calendars["calendar_collection"]
```

* **authInfo** A dict containing the URL of the login page. This code will change to also take in the ID name of the login form.

* **baseURL**  The  FQDN of your school's Sakai installation.
* **loginURL** - The url of the page where your login form is located at. This could be the homepage for the Sakai Installation or where the CAS/LDAP form is located.

* **loginFormId** The HTML id of the login form on the login page.
* **usernameField** The id of the username field for the login form.
* **passwordField** The id of the password field for the login form.

* **username** Your username.
* **password** Your password.

* import SakaiPy.RequestGenerator is the class that handles the authentication and REST requests.

* You would then define an instance of the tool you wish to use and execute the query.

As of now, it returns to you the JSON representation of the data.

### Sakai Documentation

**ALL** of the data,endpoints and documentation can be found @ <<Sakai Installation URL>>/direct/describe. 



BTW: In no way,shape,form or Universe does Rutgers University endorse or have anything to do with this library. I made it myself. This library also does not speak for the Sakai Community Project either.
