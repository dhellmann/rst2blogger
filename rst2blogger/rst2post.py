#!/usr/bin/env python
# encoding: utf-8
"""Convert an RST file to HTML suitable for posting to a blogger blog.

Requires BeautifulSoup 3.0.8.1 and docutils.

If you're a Mac user, see also http://pypi.python.org/pypi/rst2marsedit
"""

from pyquery import PyQuery

from docutils.core import publish_string

def format_post(rst_file, initial_header_level=4):
    """Read the rst file and return a tuple containing the title and
    an HTML string for the post.
    """
    with open(rst_file, 'r') as f:
        body = f.read()
    return format_post_from_string(body, initial_header_level)

def format_post_from_string(body, initial_header_level=4):
    """Returns a tuple containing the title and an HTML string for the
    post body.
    """
    try:
        html = publish_string(
            body,
            writer_name='html',
            settings_overrides={'initial_header_level':initial_header_level,
                                'generator':False,
                                'traceback':True,
                                },
            )
        if not html:
            raise ValueError('No HTML produced by docutils')
    except Exception as err:
        raise RuntimeError('Could not convert input file to HTML: %s' % err)

    # Pull out the body of the HTML to make the blog post,
    # removing the H1 element with the title.
    d = PyQuery(html, parser='html')
    title = d('body').find('h1:first').html()
    d('body').find('h1:first').remove()
    content = d('body').html()
    return title, content
