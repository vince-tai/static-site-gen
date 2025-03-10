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
                    new_nodes.append(TextNode(text, text_type if inside_text else old_node.text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if isinstance(old_node, list):
            new_nodes.extend(split_nodes_image(old_node))
        elif old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            ex_img = extract_markdown_images(old_node.text)
            if ex_img == []:
                new_nodes.append(old_node)
            else:
                for i, (img_alt, img_link) in enumerate(ex_img):
                    if i == 0:
                        sections = old_node.text.split(f"![{img_alt}]({img_link})", 1)
                    else:
                        sections = sections.split(f"![{img_alt}]({img_link})", 1)

                    new_nodes.append(TextNode(sections[0], TextType.TEXT)) # TextNode("This is text with an ", TextType.TEXT)
                    new_nodes.append(TextNode(f"{img_alt}", TextType.IMAGE, f"{img_link}"))
                    # TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")

                    if i == len(ex_img) - 1 and sections[1] != "":  # Last iteration
                        new_nodes.append(TextNode(sections[1], TextType.TEXT))
                    else:
                        sections = sections[1]
                    # and another ![second image](https://i.imgur.com/3elNhQu.png) plus maybe more

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if isinstance(old_node, list):
            new_nodes.extend(split_nodes_link(old_node))
        elif old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            ex_link = extract_markdown_links(old_node.text)
            if ex_link == []:
                new_nodes.append(old_node)
            else:
                for i, (link_alt, link_link) in enumerate(ex_link):
                    if i == 0:
                        sections = old_node.text.split(f"[{link_alt}]({link_link})", 1)
                    else:
                        sections = sections.split(f"[{link_alt}]({link_link})", 1)

                    new_nodes.append(TextNode(sections[0], TextType.TEXT)) # TextNode("This is text with an ", TextType.TEXT)
                    new_nodes.append(TextNode(f"{link_alt}", TextType.LINK, f"{link_link}"))
                    # TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")

                    if i == len(ex_link) - 1 and sections[1] != "":  # Last iteration
                        new_nodes.append(TextNode(sections[1], TextType.Text))
                    else:
                        sections = sections[1]
                    # and another ![second image](https://i.imgur.com/3elNhQu.png) plus maybe more

    return new_nodes

def text_to_textnodes(text):
    # This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
    nodes = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([nodes], "**", TextType.BOLD)
    nodes = split_nodes_delimiter([nodes], "`", TextType.CODE)
    nodes = split_nodes_delimiter([nodes], "_", TextType.ITALIC)
    nodes = split_nodes_image([nodes])
    nodes = split_nodes_link([nodes])

    return nodes