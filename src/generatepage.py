import os

from block_markdown import markdown_to_html_node

def extract_title(markdown):
    md = markdown.split("\n")
    for line in md:
        if line.startswith("# "):
            return(line[1:].strip())
    raise Exception("no title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # f= open(file_path): returns file object
    # f.read(): return the whole file
    # f.close(): close an open file
    # .replace(oldvalue, newvalue): returns modified
    # os.path.dirname(path): return a string of the path up to the dir or file
    # os.makedirs(path): make the entire path dirs
    # .startswith(stuff): return True if start with stuff
    # string.split(delimiter): return list of strings 

    with open(from_path, "r") as md:
        md_read = md.read()

    with open(template_path, "r") as temp:
        temp_read = temp.read()

    title = extract_title(md_read)

    node = markdown_to_html_node(md_read)
    html = node.to_html()

    page = temp_read.replace("{{ Title }}", title).replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok = True)

    with open(dest_path, "w") as dst:
        dst.write(page)