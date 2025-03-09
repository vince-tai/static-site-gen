from enum import Enum
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = ""):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props}>{self.value}</{self.tag}>"