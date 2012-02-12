
import tempfile

from rst2blogger.rst2post import format_post, format_post_from_string

def test_find_title():
    title, content = format_post_from_string("""
Title Goes Here
===============

this is the rest of the body
""")
    assert title == 'Title Goes Here'
    return

def test_find_body():
    title, content = format_post_from_string("""
Title Goes Here
===============

this is the rest of the body
""")
    assert 'this is the rest of the body' in content
    return

def test_file():
    f = tempfile.NamedTemporaryFile()
    f.write("""
Title Goes Here
===============

this is the rest of the body
""")
    f.flush()
    title, content = format_post(f.name)
    f.close()
    assert title == 'Title Goes Here'
    return
