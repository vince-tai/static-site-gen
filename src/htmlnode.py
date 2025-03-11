from enum import Enum

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag # "p", "a", "h1"...
        self.value = value # text content
        self.children = children # list of HTMLNode objs
        self.props = props # dict of key, value for attributes of HTML tag ({"href":"https://www.google.com"})

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self): # return props as html string
        props_html = ""

        if not self.props:
            return props_html
        
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    
    def to_html(self): # render as HTML
        if not self.value:
            raise ValueError("invalid HTML: no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    
    def to_html(self): # render self and children as HTML
        if not self.tag:
            raise ValueError("invalid HTML: no tag")
        if not self.children:
            return ValueError("invalid HTML: no children")
        
        children_value = ""

        for child in self.children:
            children_value += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_value}</{self.tag}>"