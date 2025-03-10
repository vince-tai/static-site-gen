import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if isinstance(old_node, list):
            new_nodes.extend(split_nodes_delimiter(old_node, delimiter, text_type))
        else:
            if old_node.text.count(delimiter) % 2 != 0:
                raise Exception("That's invalid Markdown syntax")
            
            esc_delimiter = re.escape(delimiter)
            split_node = re.split(f"({esc_delimiter})", old_node.text)

            inside_text = False

            for text in split_node:
                if text == delimiter:
                    inside_text = not inside_text
                else:
                    new_nodes.append(TextNode(text, text_type if inside_text else TextType.TEXT))

    return new_nodes
