import winreg as reg
import base64
import getpass
import uuid
import argon2

loc = reg.HKEY_CURRENT_USER

key = ""
enc_key = ""
def create_enc_key():
    global key, enc_key
    key = argon2.argon2_hash(uuid.getnode(), getpass.getuser())
    enc_key = base64.b64encode(key)
    print(key)
    print(enc_key)

def store_enc_key():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.CreateKey(loc_1, "WindowsUpdates")

    reg.SetValueEx(k, "key", 0, reg.REG_SZ, str(enc_key))

    if k:
        reg.CloseKey(k)

def get_enc_key():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.OpenKey(loc_1, "WindowsUpdates")
    enc_key = reg.QueryValueEx(k, "key")

    if k:
        reg.CloseKey(k)
    return enc_key

def get_token():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.OpenKey(loc_1, "WindowsUpdates")
    token = reg.QueryValueEx(k, "a")

    if k:
        reg.CloseKey(k)
    return token[0]
    
