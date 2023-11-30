import os, argon2

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

def encryptFile(file, key):
    try:
        f = open(file, 'rb')
        data = f.read()
        f.close()
        f = open(file, 'wb')
        f.write(argon2.argon2_hash(data, key))
        f.close()
    except Exception as e:
        print(e)
        return False
    return True