import os
import argon2

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

def encrypt_file(file, password):
    try:
        with open(file, 'rb') as f:
            data = f.read()
        f.close()
        with open(file, 'wb') as f:
            f.write(argon2.argon2_hash(data, password))
        f.close()
    except Exception as e:
        print(e)
        return False
    return True