import unittest
from app.block_errors import BlockErrors

class TestBlockErrors(unittest.TestCase):
    def test_ignore(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                1 / 0
        except ZeroDivisionError:
            self.fail("Should have suppressed")

    def test_not_ignored(self):
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                1 / '0'
