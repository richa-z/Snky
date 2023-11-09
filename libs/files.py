import os

def delete(file):
    try:
        os.remove(file)
    except Exception as e:
        print(e)
        return False
    return True
    


    