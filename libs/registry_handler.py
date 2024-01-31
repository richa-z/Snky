import winreg as reg
import base64
import getpass
import uuid
import random

loc = reg.HKEY_CURRENT_USER

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

key = ""
iv = ""
def create_enc_key():

    global key, enc_key
    random_string = ''.join(random.choice(letters) for i in range(16))
    key = random_string

def store_enc_key():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.CreateKey(loc_1, "WindowsUpdatesManager")

    reg.SetValueEx(k, "b", 0, reg.REG_SZ, str(key))

    if k:
        reg.CloseKey(k)

def get_enc_key():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.OpenKey(loc_1, "WindowsUpdatesManager")
    enc_key = reg.QueryValueEx(k, "b")

    if k:
        reg.CloseKey(k)
    return enc_key[0]

def create_iv():
    global iv
    iv = ''.join(random.choice(letters) for i in range(16))

def store_iv():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.CreateKey(loc_1, "WindowsUpdatesManager")

    reg.SetValueEx(k, "c", 0, reg.REG_SZ, str(iv))

    if k:
        reg.CloseKey(k)

def get_iv():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.OpenKey(loc_1, "WindowsUpdatesManager")
    iv = reg.QueryValueEx(k, "c")

    if k:
        reg.CloseKey(k)
    return iv[0]

def get_token():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.OpenKey(loc_1, "WindowsUpdatesManager")
    token = reg.QueryValueEx(k, "a")

    if k:
        reg.CloseKey(k)
    return token[0]
