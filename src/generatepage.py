import os

from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    md = markdown.split("\n")
    for line in md:
        if line.startswith("# "):
            return(line[1:].strip())
    raise Exception("no title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md:
        md_read = md.read()

    with open(template_path, "r") as temp:
        temp_read = temp.read()

    title = extract_title(md_read)

    node = markdown_to_html_node(md_read)
    html = node.to_html()

    page = temp_read.replace("{{ Title }}", title).replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok = True)

    name, _ = os.path.splitext(dest_path)
    dest_path = name + ".html"

    with open(dest_path, "w") as dst:
        dst.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_path = Path(dir_path_content)
    dst_path = Path(dest_dir_path)
    temp_path = Path(template_path)

    for item in os.listdir(content_path):
        item_content_path = os.path.join(content_path, item)
        item_dst_path = os.path.join(dst_path, item)

        if os.path.isfile(item_content_path):
            generate_page(item_content_path, temp_path, item_dst_path)
            continue
        generate_pages_recursive(item_content_path, temp_path, item_dst_path)