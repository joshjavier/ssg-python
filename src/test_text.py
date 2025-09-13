import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


class TestText(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://joshjavier.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://joshjavier.com"})
        self.assertEqual(html_node.value, "This is a link node")

    def test_image(self):
        node = TextNode(
            "This is an image node",
            TextType.IMAGE,
            "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {
                "src": "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png",
                "alt": "This is an image node",
            },
        )

    def test_no_type(self):
        with self.assertRaisesRegex(Exception, "^invalid TextType$"):
            node = TextNode("This node has no `text_type` field", None)
            html_node = text_node_to_html_node(node)
