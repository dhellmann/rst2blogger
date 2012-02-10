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
