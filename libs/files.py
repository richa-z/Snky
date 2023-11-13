import os

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