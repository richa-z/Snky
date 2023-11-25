import os
from cryptography.fernet import Fernet

def delete(file):
    try:
        os.remove(file)
    except Exception as e:
        print(e)
        return False
    return True

def delete_dir(dir):
    try:
        os.rmdir(dir)
    except Exception as e:
        print(e)
        return False
    return True

def create_dir(dir):
    try:
        os.mkdir(dir)
    except Exception as e:
        print(e)
        return False
    return True

def encrypt_file(file, key):
    try:
        with open(file, "rb") as f:
            data = f.read()
        with open(file, "wb") as f:
            f.write(encrypt(data, key))
    except Exception as e:
        print(e)
        return False
    return True

def decrypt_file(file, key):
    try:
        with open(file, "rb") as f:
            data = f.read()
        with open(file, "wb") as f:
            f.write(decrypt(data, key))
    except Exception as e:
        print(e)
        return False
    return True

def encrypt(data, key):
    f = Fernet(key)
    with open(bytes(data), "rb") as F:
        file = f.read()
        enc_data = f.encrypt(file)
    
    with open(bytes(data), "wb") as F:
        F.write(enc_data)

def decrypt(data, key):
    f = Fernet(key)
    with open(data, "rb") as F:
        file = f.read()
        dec_data = f.decrypt(file)
    
    with open(data, "wb") as F:
        F.write(dec_data)
