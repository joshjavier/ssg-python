import re
from enum import Enum


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = [block.strip() for block in blocks]
    non_empty_blocks = []
    for block in stripped_blocks:
        if block:
            non_empty_blocks.append(block)
    return non_empty_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    heading = re.compile(r"^#{1,6} .+$")
    code = re.compile(r"^\s*```.*\n.*\n\s*```\s*$")
    quote = re.compile(r"^> .+$", re.MULTILINE)

    if heading.match(block):
        return BlockType.HEADING

    if code.match(block):
        return BlockType.CODE

    if quote.search(block):
        return BlockType.QUOTE

    return BlockType.PARAGRAPH
