import os

def dir(directory):
    return str(os.listdir(directory))

def tasklist():
    os.popen("tasklist > tasklist.txt")
    
def taskkill(process):
    if os.popen(f"taskkill /im {process} /f") == 0:
        result = f"Process {process} killed."
        return result
    else:
        result = f"Failed to kill process {process}."
        return result


    
