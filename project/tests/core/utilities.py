from ctypes import util
import unittest
from project.core import utilities


class TestUtilities(unittest.TestCase):
    def test_hello(self):
        result = utilities.hello("world")
        self.assertEqual(result, "Hello world")
