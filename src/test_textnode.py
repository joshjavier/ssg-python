import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("Windows", TextType.PLAIN)
        node2 = TextNode("Linux", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("Boot.dev", TextType.BOLD)
        node2 = TextNode("Boot.dev", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
