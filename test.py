import winreg as reg

loc = reg.HKEY_CURRENT_USER

def get_key():
    loc_1 = reg.OpenKeyEx(loc, r"SOFTWARE\\")
    k = reg.OpenKey(loc_1, "WindowsUpdates")
    key = reg.QueryValueEx(k, "b")

    if k:
        reg.CloseKey(k)
    return str(key[0])

print(get_key())