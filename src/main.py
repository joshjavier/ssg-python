import os

from lib.page import generate_page, generate_pages
from static import copy_static


def main():
    print("Copying files in `static` directory...")
    files_copied = copy_static("static", "public")
    if files_copied:
        print(f"{files_copied} files copied.")
    else:
        print("Nothing to copy.")

    generate_pages("content", "public")


if __name__ == "__main__":
    main()
