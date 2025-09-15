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
    code = re.compile(r"^```.*\n(.*\n)*\s*```$")
    quote = re.compile(r"^> .+$", re.MULTILINE)
    unordered_list = re.compile(r"^\s*- .+$", re.MULTILINE)
    ordered_list = re.compile(r"^\s*\d+\. .+$", re.MULTILINE)

    if heading.match(block):
        return BlockType.HEADING

    if code.match(block):
        return BlockType.CODE

    if quote.search(block):
        return BlockType.QUOTE

    if unordered_list.search(block):
        return BlockType.UNORDERED_LIST

    if ordered_list.search(block):
        lines = [line.strip() for line in block.split("\n")]
        for i in range(len(lines)):
            number, _ = lines[i].split(".", 1)
            number = int(number)
            if i == 0:
                if number != 1:
                    return BlockType.PARAGRAPH
            elif number != i + 1:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
