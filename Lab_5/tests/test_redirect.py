import unittest
from io import StringIO
from app.redirect import Redirect

class TestRedirect(unittest.TestCase):
    def test_stdout(self):
        buf = StringIO()
        with Redirect(stdout=buf):
            print("hello")
        self.assertIn("hello", buf.getvalue())

    def test_stderr(self):
        buf = StringIO()
        try:
            with Redirect(stderr=buf):
                raise ValueError("oops")
        except ValueError:
            pass
        self.assertIn("ValueError", buf.getvalue())
