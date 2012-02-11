.. -*- mode: rst -*-

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

Features
========

* Quickly and easily publish reStructuredText source files as blog posts on blogger.com
* Publish to any blogger.com blog
* Update the text of existing posts with new drafts

Installation
============

Download the latest release from `the PyPI page`_.

See `the project documentation`_ for installation and setup instructions.

.. _the project documentation: http://www.doughellmann.com/docs/rst2blogger/

.. _the PyPI page: http://pypi.python.org/pypi/rst2blogger

Support
=======

This project is hosted on github.com: https://github.com/dhellmann/rst2blogger

Please report issues via the `bug tracker`_.

.. _bug tracker: https://github.com/dhellmann/rst2blogger/issues

License
=======

Copyright 2012 Doug Hellmann, All Rights Reserved

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Doug Hellmann not be
used in advertising or publicity pertaining to distribution of the
software without specific, written prior permission.

DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
