SakaiPy
=======

A library to access the information located on Sakai installations. This can be thought more of a 'pretty wrapper' around the REST interface that Sakai gives you.

I'm mainly a Java developer so anyone with more Python experience is more than welcome to make a pull request to clean it up!

I made this library so people can access the Sakai information at their schools (I'm @ Rutgers) more easily through Python.

You can install SakaiPy with pip by typing in the following command:

```
pip install SakaiPy
```

I'll usually make a blog post about each new version at my website. https://blog.willkara.com

### TO-DO
* Integrate services available under Sakai's WebServices directory.
* Add events to Google Calendar.
* Add more Sakai tools and more functionality for each tool.
* Better HTTP Code error handling- If something breaks return a code, or a reason depending on how Sakai handles the error.

### Example

````
from SakaiPy import SakaiPy

info = {'username': 'willkara',
        'password': '8675309eeine',
        'baseurl': 'https://sakai.rutgers.edu'}

sak = SakaiPy.SakaiPy(info)

print(sak.session.get_current_user_info())
```

### Sakai Documentation

**ALL** of the data,endpoints and documentation can be found @ <<Sakai Installation URL>>/direct/describe. 



BTW: In no way,shape,form or Universe does Rutgers University endorse or have anything to do with this library. I made it myself. This library also does not speak for the Sakai Community Project either.
