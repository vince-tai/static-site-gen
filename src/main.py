from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    text_value = text_node.text

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, value = text_value)

        case TextType.BOLD:
            return LeafNode("b", text_value)

        case TextType.ITALIC:
            return LeafNode("p", text_value)

        case TextType.CODE:
            return LeafNode("p", text_value)

        case TextType.LINK:
            return LeafNode("a", text_value)

        case TextType.IMAGE:
            return LeafNode("img", "", {"src": "image url", "alt": "alt text"})

        case _:
            raise Exception("Invalid text type")

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

main()