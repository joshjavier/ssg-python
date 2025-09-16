import os
import shutil


def copy_static(source, dest, is_root=True):
    source = os.path.abspath(source)
    dest = os.path.abspath(dest)
    files_copied = 0

    if is_root:
        if os.path.exists(dest):
            shutil.rmtree(dest)
        os.mkdir(dest)

    entries = os.listdir(source)
    for entry in entries:
        childpath = os.path.join(source, entry)
        if os.path.isdir(childpath):
            destpath = os.path.join(dest, entry)
            os.mkdir(destpath)
            files_copied += copy_static(childpath, destpath)
        else:
            shutil.copy(childpath, dest)
            files_copied += 1

    return files_copied
