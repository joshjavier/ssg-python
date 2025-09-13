from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            raise Exception("parsing TextType other than TEXT is not yet implemented")

        segments = node.text.split(delimiter)
        for i in range(len(segments)):
            # segments at even indices are text segments,
            # while segments at odd indices are `text_type`
            new_node = TextNode(segments[i], text_type if i % 2 != 0 else TextType.TEXT)
            new_nodes.append(new_node)
    return new_nodes
