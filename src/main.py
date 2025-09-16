from static import copy_static


def main():
    print("Copying files in `static` directory...")
    files_copied = copy_static("static", "public")
    if files_copied:
        print(f"{files_copied} files copied.")
    else:
        print("Nothing to copy.")


if __name__ == "__main__":
    main()
