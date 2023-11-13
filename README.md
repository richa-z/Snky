# Snky - A basic Discord bot-based RAT.
****Project is for educational purposes only.****

Written in Python and Batch.
## Features
Bot is in constant development and they may be new features or changes to the old ones.

Current commands:
- **.pcinfo** - Fetch information about the computer using the ```systeminfo``` command in command prompt.
- **.hardware** - Fetch information about the computer's hardware using WMIC. [GPU/CPU Name, HWID, RAM Capacity, Disk Capacity]
- **.shutdown** - Shutdown the computer.
- **.dir** - List the specified directory's files. Usage: ```.dir <full path>```
- **.tasklist** - List all tasks with a specific name. Usage: ```.tasklist <program name>```. Example: ```.tasklist opera.exe```
- **.taskkill** - Kill a specified task. Usage: ```.taskkill <PID>```
- **.screenshot** - Take a screenshot.
- **.copy** - Copy a specified file. Usage: ```.copy <full file path>```. Example: ```.copy c:/Users/user/Desktop/textfile.txt```
- **.bsod** - Trigger a BSOD.
- **.webcam** - Take a picture using the webcamera.
- **.logout** - Logout the user from the computer.
- **.delete** - Delete a specified file. Usage: ```.delete <full file path>```. Example: ```.delete c:/Users/user/Desktop/textfile.txt```
- **.blockinput** - Block all input from the user's keyboard and mouse.
- **.unblockinput** - Unblock all input from the user's keyboard and mouse.
- **.selfdestruct** - Run a .bat file that removes the bot and all it's features from the computer.
- **.deletedir** - Delete a directory. Usage: ```.deletedir <full dir path>```. Example: ```.deletedir c:/Users/user/Desktop/MyFolder```
- **.createdir** - Create a directory. Usage: ```.createdir <new dir path>```. Example ```.createdir c:/Users/user/Desktop/MyNewFolder```
- **.modules** - List/run modules in the ```/modules``` folder. Usage: ```.modules <list/load>```

This project supports custom modules. If you want to add your own script (not a command), create it and put it into the ```/modules``` folder. The bot runs these when launching itself.
