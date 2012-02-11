=============
 rst2blogger
=============

rst2blogger is a command line program for converting reStructuredText_
documents to HTML suitable for posting to blogger.com.  It takes as
input a single filename and an optional blog title. The input file is
parsed with docutils_ to create HTML, and the HTML is uploaded as a
draft to the specified blog.  If the blogger account only has one
blog, the name does not need to be specified.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

.. _docutils: http://docutils.sourceforge.net/

Installation
============

The simplest way to install rst2blogger is using pip::

  $ pip install rst2blogger

You can also download the latest release from `the PyPI page`_ and
install it by hand::

  $ tar zxf rst2blogger-*.tar.gz
  $ cd rst2blogger*
  $ python setup.py install

.. _the PyPI page: http://pypi.python.org/pypi/rst2blogger

Usage
=====

Usage::

  rst2blogger [-h] [-b BLOG] filename

-h
  Show the command help.

-b, --blog
  Specify the blog where the new post should be uploaded.

filename
  The name of the input reStructuredText file.

Authentication
--------------

rst2blogger authenticates with the Blogger API interactively after
parsing the input file.

Input File Format
-----------------

The input reStructuredText file should have a single top-level heading
to be used as the title of the post. That value is stripped from the
HTML body of the post, but other headings and structures such as
tables and lists are included.

Identifying Blogs
-----------------

The ``-b`` and ``--blog`` options to the ``rst2blogger`` command take
as argument the title of the blog to receive the new post. If the
authenticated account only has access to one blog, it does not need to
be specified on the command line. If a blog title is required but not
provided, the program prints a list of the available blogs and exits
with an error.

History
=======

1.0

 - Initial public release

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

