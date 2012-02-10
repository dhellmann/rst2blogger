#!/usr/bin/env python
# encoding: utf-8
"""Convert an RST file to HTML suitable for posting to the PSF blog.

Requires BeautifulSoup 3.0.8.1 and docutils.

If you're a Mac user, see also http://pypi.python.org/pypi/rst2marsedit
"""

import codecs
import optparse
import os
import sys
import string
import subprocess
import tempfile

from BeautifulSoup import BeautifulSoup

def format_post(rst_file):
    """Read the rst file and return a tuple containing the title and
    an HTML string for the post.
    """
    rst_args = ['--no-generator', '--initial-header-level=4', rst_file]
    if sys.platform == 'win32':
        exe = [sys.executable,
               os.path.join(os.path.dirname(sys.executable),
                            'Scripts', 'rst2html.py')]
    else:
        exe = ['rst2html.py']

    # Convert RST to HTML
    try:
        rst2html = subprocess.Popen(exe + rst_args,
                                    stdout=subprocess.PIPE)
        html = rst2html.communicate()[0]
        if not html:
            raise ValueError('No HTML produced by rst2html.py')
    except Exception, err:
        raise RuntimeError('Could not convert input file to HTML with rst2html.py: %s' % str(err))
    soup = BeautifulSoup(html)

    # Pull out the body of the HTML to make the blog post,
    # removing the H1 element with the title.
    body = soup.find('body')
    title = ''.join(' '.join(unicode(c) for c in h1.extract().contents)
                    for h1 in body.findAll('h1'))
    content = ''.join(unicode(c) for c in body.contents).strip()
    return title, content

def main():
    parser = optparse.OptionParser('%prog <infile>')
    options, args = parser.parse_args()

    if not args:
        parser.error('Please specify an input rst file')
    
    title, content = format_post(args[0])
    stdout_encoding = sys.stdout.encoding or sys.getfilesystemencoding()
    print content.encode(stdout_encoding)
    return


if __name__ == '__main__':
    main()
