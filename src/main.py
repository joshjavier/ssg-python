from lib.generator import generate_pages_recursive
from static import copy_static


def main():
    print("Copying files in `static` directory...")
    files_copied = copy_static("static", "public")
    if files_copied:
        print(f"{files_copied} files copied.")
    else:
        print("Nothing to copy.")

    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
