import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TextSplitDelimiter(unittest.TestCase):
    def test_new_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, nodes)

    def test_new_nodes(self):
        old_nodes = [
            TextNode("This is text with a code block word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter([old_nodes], "`", TextType.CODE)
        nodes = [
            TextNode("This is text with a code block word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, nodes)

    def test_new_bold_nodes(self):
        old_nodes = [
            TextNode("This is text with a **bold** word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text with a _italic_ word", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter([old_nodes], "**", TextType.BOLD)
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text with a _italic_ word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, nodes)

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

if __name__ == "__main__":
    unittest.main()