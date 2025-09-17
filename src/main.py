import sys

from lib.generator import generate_pages_recursive
from static import copy_static


def main(input, output, layout, basepath):
    print("Copying files in `static` directory...")
    files_copied = copy_static("static", output)
    if files_copied:
        print(f"{files_copied} files copied.")
    else:
        print("Nothing to copy.")

    generate_pages_recursive(input, layout, output, basepath)


if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) == 2 else "/"
    input = "content"
    output = "docs"
    layout = "template.html"
    main(input, output, layout, basepath)
