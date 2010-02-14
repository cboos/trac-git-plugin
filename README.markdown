trac-git-plugin
===============

This is a port of [GitPlugin](http://www.trac-hacks.org/wiki/GitPlugin) for
Trac 0.12.


Current Status
--------------

The plugin seems to be working well at the moment.  Multi-repository support
is working, as are both the cached and uncached repository options.  Some
parts might still be a little rough around the edges though :)


Getting Started
---------------

You might want to use a [virtualenv](http://pypi.python.org/pypi/virtualenv)
to try the plugin out for the first time.  After setting up a new environment
you can install the current development version of Trac:

    easy_install genshi==dev
    easy_install trac==dev

Then install the plugin:

    python setup.py install

Create a new Trac environment by running `trac-admin [DIR] initenv`, and then
set the path to your git executable in `[DIR]/conf/trac.ini` by adding the
following (with the correct path for your system, of course):

    [git]
    git_bin = /usr/local/git/bin/git

At this point you should be able to start the Trac instance using your normal
methods, and use the admin page to enable the plugin and add references to
your git repositories.

For more information on the configuration options available, see the GitPlugin
link above.
