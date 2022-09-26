import os


def remove_files(root, pattern="."):
    walk = os.walk(root)

    for root, folder, files in walk:
        for file in files:
            if file.startswith(pattern):
                file_path = os.path.join(root, file)
                os.remove(file_path)
