def markdown_to_blocks(markdown):
    new_md = []

    split_md = markdown.split("\n\n")

    for block in split_md:
        strip_block = block.strip()
        if block != "":
            new_md.append(strip_block)

    return new_md