import unittest

from lib.page import extract_title

class TestPage(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Hello this is a title
"""
        title = extract_title(md)
        self.assertEqual(title, "Hello this is a title")

    def test_extract_title_exception(self):
        md = """
## Hello this is not a title
"""
        with self.assertRaises(Exception):
            extract_title(md)
