import os

def dir(directory):
    return str(os.listdir(directory))

def tasklist(process):
    result = ""
    if process != "":
        result = str(os.popen(f"tasklist | findstr {process}").read())
        return result
    else:
        result = "Specify a process name to return."
        return result
    
def taskkill(process):
    if os.system(f"taskkill /im {process} /f") == 0:
        result = f"Process {process} killed."
        return result
    else:
        result = f"Failed to kill process {process}."
        return result
    
