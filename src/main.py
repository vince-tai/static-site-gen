import shutil
import os
import sys

from copystatic import copy
from generatepage import generate_pages_recursive

def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    # Dynamically find the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    # # Define absolute paths dynamically
    static_path = os.path.join(project_root, "static")
    docs_path = os.path.join(project_root, "docs")
    
    if os.path.exists(docs_path):
        print("Removing stuff...")
        shutil.rmtree(docs_path)

    copy(static_path, docs_path)

    from_path = os.path.join(project_root, "content")
    template_path = os.path.join(project_root, "template.html")

    generate_pages_recursive(from_path, template_path, docs_path, base_path)

main()