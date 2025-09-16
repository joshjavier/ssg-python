from lib.page import generate_page
from static import copy_static


def main():
    print("Copying files in `static` directory...")
    files_copied = copy_static("static", "public")
    if files_copied:
        print(f"{files_copied} files copied.")
    else:
        print("Nothing to copy.")

    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
