SakaiPy
=======

A library to access the information located on Sakai installations. This can be thought more of a 'pretty wrapper' around the REST interface that Sakai gives you.

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

With the changes of how Sakai handles logins and a rewrite of the architecture I've had to get rid of the examples. Of course I'll post all the info once I have everything figured out.

### Sakai Documentation

**ALL** of the data,endpoints and documentation can be found @ <<Sakai Installation URL>>/direct/describe. 



BTW: In no way,shape,form or Universe does Rutgers University endorse or have anything to do with this library. I made it myself. This library also does not speak for the Sakai Community Project either.
