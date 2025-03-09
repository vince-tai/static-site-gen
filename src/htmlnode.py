from enum import Enum

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        for a in self.props:
            html += f' {a}="{self.props[a]}"'
        return html
    
    def __repr__(self):
        print(f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}")