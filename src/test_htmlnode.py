import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node.tag, node2.tag)

    def test_not_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("div")
        self.assertNotEqual(node, node2)
    
    def test_props_to_html(self):
        prop = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        node = HTMLNode("p", props = prop)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()