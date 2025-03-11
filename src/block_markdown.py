import re

from block import BlockType
from htmlnode import HTMLNode
from textnode import TextNode, text_node_to_html_node

def markdown_to_blocks(markdown):
    blocks = []

    split_md = markdown.split("\n\n")

    for block in split_md:
        strip_block = block.strip()
        if block != "":
            blocks.append(strip_block)

    return blocks

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")
    quote_check = True
    ul_check = True
    ol_check = True
    for i, (line) in enumerate(lines):
        if not line.startswith(">"):
            quote_check = False
        if not line.startswith("- "):
            ul_check = False
        if not re.search(rf"^{i + 1}\.", line):
            ol_check = False
        i += 1
    
    if quote_check == True:
        return BlockType.QUOTE

    if ul_check == True:
        return BlockType.ULIST
    
    if ol_check == True:
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH

# def markdown_to_html_node(markdown):
#     blocks = markdown_to_blocks(markdown)
#     for block in blocks:
#         block_type = block_to_block_type(block)
#         match block_type:
#             case BlockType.PARAGRAPH:
#                 block_node = HTMLNode("<p>", block)
#                 text_to_children(block)
#             case BlockType.HEADING:
#                 block_node = HTMLNode("")
#             case BlockType.CODE:
#                 node = TextNode("")
#                 node = text_node_to_html_node(block)
#             case 


#     return html_node

# def text_to_children(text):


#     return html_nodes