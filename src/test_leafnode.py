import unittest

from leafnode import LeafNode


class TestLeadNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

if __name__ == "__main__":
    unittest.main()