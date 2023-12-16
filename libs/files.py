import os
from Cryptodome.Cipher import AES

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

def encrypt_file(file, password, iv):
    try:
        password = str(password)
        iv = str(iv)
        print(password)
        print(iv)
        with open(file, "rb") as f:
            data = f.read()
        cipher = AES.new(password.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
        encrypted_data = cipher.encrypt(data)
        with open(file, "wb") as f:
            f.write(encrypted_data)
    except Exception as e:
        print(e)
        return False
    return True

def decrypt_file(file, password, iv):
    try:
        with open(file, "rb") as f:
            data = f.read()
        cipher = AES.new(password, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(data)
        with open(file, "wb") as f:
            f.write(decrypted_data)
    except Exception as e:
        print(e)
        return False
    return True

        