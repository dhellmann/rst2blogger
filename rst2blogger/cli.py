#!/usr/bin/env python
# encoding: utf-8
"""Convert an RST file to HTML and push the post up to blogger as a draft.

Requires BeautifulSoup 3.0.8.1, docutils, and gdata.

If you're a Mac user, see also http://pypi.python.org/pypi/rst2marsedit
"""

# stdlib
import argparse
import codecs
import datetime
import locale
import sys

# third-party
import gdata.blogger.client
import gdata.client
import gdata.sample_util
import gdata.service
import gdata.data
import atom.data

# local
import rst2post

def main():
    parser = argparse.ArgumentParser(description='Blogger client')
    parser.add_argument('-b', '--blog', action='store',
                        help='title of the blog to receive the new draft')
    parser.add_argument('filename', action='store',
                        help='reST input file')
    options = parser.parse_args()

    # Set up console encoding
    locale.setlocale(locale.LC_ALL, '')
    lang, encoding = locale.getdefaultlocale()
    if not hasattr(sys.stdout, 'encoding'):
        sys.stdout = codecs.getwriter(encoding)(sys.stdout)
    if not hasattr(sys.stderr, 'encoding'):
        sys.stderr = codecs.getwriter(encoding)(sys.stderr)

    # Start by parsing the file locally in case there is a problem
    # and we can avoid the authentication step.
    post_title, post_content = rst2post.format_post(options.filename)
    print "\nTitle: '%s'\n" % post_title

    # Authenticate using ClientLogin, AuthSub, or OAuth.
    client = gdata.blogger.client.BloggerClient()
    for i in range(3):
        try:
            gdata.sample_util.authorize_client(
                client, service='blogger', source='rst2blogger.py',
                scopes=['http://www.blogger.com/feeds/'])
        except (ValueError, gdata.client.BadAuthentication) as err:
            print
            print 'Failed to authenticate:', err
            print
        else:
            break
    else:
        raise RuntimeError, 'Authentication failure'

    # Get the ID for the blog
    print 'Retreiving blog list'
    feed = client.get_blogs()
    blogs_by_title = dict( (b.title.text, b)
                           for b in feed.entry
                           )
    if not options.blog:
        if len(blogs_by_title.keys()) == 1:
            options.blog = blogs_by_title.keys()[0]
        else:
            print 'Available blogs:'
            for t in sorted(blogs_by_title.keys()):
                print u'- %s' % t
            print
            raise RuntimeError, 'Please specify the blog title with --blog'
    target_blog = blogs_by_title[options.blog]
    target_blog_id = target_blog.get_blog_id()

    # We will look for a post with the same title in the last week, in
    # case this is a work-in-progress that needs to be updated. We
    # limit the search to a week because we do not want to update
    # really old posts with similar titles.
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    week_ago = today - datetime.timedelta(days=7)
    query = gdata.blogger.client.Query(updated_min=str(week_ago),
                                       updated_max=str(tomorrow),
                                       order_by='updated')

    # Determine if there is a post with this title already
    print 'Looking for existing post to be updated'
    feed = client.get_posts(target_blog_id, query=query)
    existing_posts = [ entry
                       for entry in feed.entry
                       if entry.title.text == post_title
                       ]
    if existing_posts:
        if len(existing_posts) > 1:
            raise ValueError('Found multiple posts with the same title!')
        print 'Updating existing post'
        post_to_update = existing_posts[0]
        post_to_update.title = atom.data.Title(type='xhtml', text=post_title)
        post_to_update.content = atom.data.Content(type='html', text=post_content)
        client.update(post_to_update)
    else:
        # The post was not found, so make a new one
        print 'Creating new post'
        new_post = client.add_post(target_blog_id, post_title, post_content, draft=True)
    print 'Uploaded new draft'
    return

if __name__ == '__main__':
    main()
    
