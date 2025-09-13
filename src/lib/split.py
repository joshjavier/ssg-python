from lib.regex import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        segments = old_node.text.split(delimiter)
        if len(segments) % 2 == 0:
            raise Exception(
                "Invalid markdown syntax: Matching closing delimiter not found."
            )
        for i in range(len(segments)):
            # segments at even indices are text segments,
            # while segments at odd indices are `text_type`
            new_node = TextNode(segments[i], text_type if i % 2 != 0 else TextType.TEXT)
            new_nodes.append(new_node)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        for image_alt, image_link in images:
            # add nodes for each extracted image and the text before it
            first_segment, original_text = original_text.split(
                f"![{image_alt}]({image_link})", 1
            )
            if first_segment:
                split_nodes.append(TextNode(first_segment, TextType.TEXT))
            split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
        # add remaining text if any
        if original_text:
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        for link_anchor, link_href in links:
            # add nodes for each extracted link and the text before it
            first_segment, original_text = original_text.split(
                f"[{link_anchor}]({link_href})", 1
            )
            if first_segment:
                split_nodes.append(TextNode(first_segment, TextType.TEXT))
            split_nodes.append(TextNode(link_anchor, TextType.LINK, link_href))
        # add remaining text if any
        if original_text:
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes
