import unittest

from generatepage import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")