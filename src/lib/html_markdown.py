from lib.block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from lib.inline_markdown import text_to_textnodes
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def markdown_to_html_node(markdown):
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    root_children = []
    # Loop over each block
    for block in blocks:
        # Determine the type of block
        block_type = block_to_block_type(block)

        # Based on the type of block, create a new HTMLNode with the proper data
        if block_type is BlockType.PARAGRAPH:
            children = text_to_children(block)
            node = ParentNode("p", children)
            root_children.append(node)

        elif block_type is BlockType.HEADING:
            hash, content = block.split(maxsplit=1)
            children = text_to_children(content)
            node = ParentNode(f"h{len(hash)}", children)
            root_children.append(node)

        elif block_type is BlockType.UNORDERED_LIST:
            lines = [line.strip() for line in block.split("\n")]
            list_items = []
            for line in lines:
                _, content = line.split(maxsplit=1)
                children = text_to_children(content)
                li = ParentNode("li", children)
                list_items.append(li)
            ul = ParentNode("ul", list_items)
            root_children.append(ul)

        elif block_type is BlockType.ORDERED_LIST:
            lines = [line.strip() for line in block.split("\n")]
            list_items = []
            for line in lines:
                _, content = line.split(". ", 1)
                children = text_to_children(content)
                li = ParentNode("li", children)
                list_items.append(li)
            ol = ParentNode("ol", list_items)
            root_children.append(ol)

        elif block_type is BlockType.QUOTE:
            text = "\n".join([line[2:] for line in block.split("\n")])
            children = text_to_children(text)
            node = ParentNode("blockquote", children)
            root_children.append(node)

        # The "code" block is a bit of a special case: it should **not** do any inline markdown parsing of its children.
        elif block_type is BlockType.CODE:
            text_node = TextNode(block, TextType.CODE)
            code_node = text_node_to_html_node(text_node)
            node = ParentNode("pre", [code_node])
            root_children.append(node)

    # Make all the block nodes children under a single parent HTML node (which should just be a div) and return it
    return ParentNode("div", root_children)
