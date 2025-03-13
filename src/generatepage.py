def extract_title(markdown):
    md = markdown.split("\n")
    for line in md:
        if line.startswith("# "):
            return(line[1:].strip())
    raise Exception("no title")