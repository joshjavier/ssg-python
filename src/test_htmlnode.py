import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        a = HTMLNode(
            "a",
            "Hello, world!",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        html = a.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com" target="_blank"')

    def test_no_props(self):
        div = HTMLNode("div", "Propless Node")
        html = div.props_to_html()
        self.assertEqual(html, "")

    def test_to_html(self):
        div = HTMLNode("div")
        self.assertRaises(NotImplementedError, div.to_html)


if __name__ == "__main__":
    unittest.main()
