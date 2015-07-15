Python Talk: Setuptools and Web Scraping
========================================

On July 15, 2015, I spoke with the Alamo Python Learners about Python. This
repository contains the code we wrote together during the talk, and a few
notes for those who may be looking at the code afterwards figuring out what we
did and where to find more information.

Quick Summary of My Talk
------------------------

Programming can be a lot of fun, and I believe the best way to learn is to
program something that is interesting to you personally. For me, that
something was often chess related. Since I understand not everyone here may be
into chess, today I wanted to talk about web scraping. Personally, I have used
web scraping to gather information about chess openings, sports teams and real
estate.

The basic idea is to programmatically crawl one or more web pages, extract the
information that interest you, and then output that information in a desired
format. What you do with the information next is up to you, for fun or profit.

Before jumping into that, I also want to introduce you to the [setuptools]
package. With setuptools, you can easily build and distribute the packages you
create in a standard way. It's not something you'll need for every project.
Certainly this simple example could be done without it, but it is helpful when
you start working with other developers to follow certain standards.

You can see in our example, we created a setup.py file describing the Python
package. We indicated it depends on other packages. We could be more specific
about the version of the packages it requires. We also define an entry point
which is how we will run our program. This example only scratches the surface
of setuptools. You could also define tests, data files and more.

Looking at our actual program, you can see there's not a lot of code required.
Others have written packages to get via HTTP and to parse HTML documents. In
this example, we use the [requests] package to get the web page, and the
[lxml] package to parse and then extracts the text using [xpath].

This pretty simple example extracts some specific text from a single page. If
you want to get more advanced and crawl multiple pages, you should checkout
[scrapy].

Now, go and scrape something you find interesting, or write an entirely
different program and share it on [pypi]. Most importantly, have fun!

[setuptools]: https://pythonhosted.org/setuptools/
[requests]:   http://docs.python-requests.org
[lxml]:       http://lxml.de/lxmlhtml.html
[xpath]:      http://lxml.de/xpathxslt.html
[scrapy]:     http://scrapy.org
[pypi]:       https://pypi.python.org/pypi

Developer Instructions
----------------------

To setup your development environment and run the program:

```
$ python setup.py develop
$ applewatch
```

Installation Instructions
-------------------------

To install the program, so you can run it anywhere:

```
$ python setup.py install
```
