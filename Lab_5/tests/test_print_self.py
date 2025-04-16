import unittest
from app.print_self import PrintSelf
from io import StringIO
import sys

class TestPrintSelf(unittest.TestCase):
    def test_repr(self):
        buf = StringIO()
        sys.stdout = buf
        obj = PrintSelf("Hello from __repr__")
        repr(obj)
        sys.stdout = sys.__stdout__
        self.assertIn("Hello from __repr__", buf.getvalue())
