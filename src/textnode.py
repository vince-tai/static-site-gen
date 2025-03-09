from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        if (self.text == node.text
            and self.text_type == node.text_type
            and self.url == node.url
        ):
            return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    text_value = text_node.text

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value = text_value)

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