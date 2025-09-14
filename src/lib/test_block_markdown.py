import unittest

from lib.block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_heading(self):
        block = "# This is a level 1 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "####### No such thing as a level 7 heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_code(self):
        block = """```
This is a code block
```
"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = """
```
This is also a code block
```
"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = """
        ```
        This is yet another code block
        ```
        """
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
