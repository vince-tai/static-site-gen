import shutil
import os

from copystatic import copy
from generatepage import generate_pages_recursive

def main():
    # Dynamically find the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    # Define absolute paths dynamically
    static_path = os.path.join(project_root, "static")
    public_path = os.path.join(project_root, "public")

    shutil.rmtree(public_path)
    copy(static_path, public_path)

    from_path = os.path.join(project_root, "content")
    template_path = os.path.join(project_root, "template.html")

    generate_pages_recursive(from_path, template_path, public_path)

main()