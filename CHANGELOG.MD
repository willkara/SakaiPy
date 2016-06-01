# Change Log

### 2.2.0

SakaiPy works again! I was able to find a more stable way of creating sessions! Now I'll be able to base all future work off of a stable platform.

 * New way to handle session generation.
 * Architecture re-write to work with new session generation.

### 2.1.0

Since this is a pretty major rewrite (and I didn't feel like making a v3) I'll be making a post about this rewrite at my blog. I'm also in the the process of trying to automatically host documentation for SakaiPy.

 * Complete rewrite of the program architecture. Documentation for API incoming.
 * Introduce SakaiPy object. This object is now the main entry point for the library.

### 2.0.0
 * Should work with Python3.x correctly.
 * No longer uses mechanize for web-scraping/login form.
 * Uses the /session REST api for session cookies.

### 1.2.0
 * Implemented some HTTP error checking for the requests. Still need to implement some sort of error checking for the login portion.

### 1.1.1
 * Only works in 2.7 currently. Mechanize does not yet support 3.x

### 1.1.0
 * Added ability to specify login form id and username/password field names
 * Any Sakai installation should technically be able to use it now
 

