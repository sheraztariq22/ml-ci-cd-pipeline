import unittest
from app import app


class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")
