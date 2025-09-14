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
        block = markdown_to_blocks("# This is a level 1 heading")[0]
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = markdown_to_blocks("####### No such thing as a level 7 heading")[0]
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_code(self):
        md = """```
This is a code block
```
"""
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        md = """
```
This is also a code block
```
"""
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        md = """
        ```
        This is yet another code block
        ```
        """
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_quote(self):
        md = """
> This is a quote.
> - by me
"""
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        md = """
        > This is also a quote block.
        > - by me
        """
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_unordered_list(self):
        md = """
- This is a list
- with items
"""
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        md = """
        - This is also a list
        - with items
        """
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        md = "- This is a list with one item"
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_ordered_list(self):
        md = """
1. This is an ordered list
2. with items
"""
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        md = """
        1. This is also an ordered list
        2. with items
        """
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        md = "2. An ordered list must start at 1"
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        md = """
        1. An ordered list must
        3. increment by 1 for each line
        """
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_paragraph(self):
        md = "This is a normal paragraph"
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        md = """
        This is a normal
        multiline paragraph
        """
        block = markdown_to_blocks(md)[0]
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
