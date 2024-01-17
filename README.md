# Snky - A basic Discord bot-based RAT.
****Project is for educational purposes only.****

Written in Python, Batch and Powershell.
Written by: [@richa-z](https://github.com/richa-z) & [@mart1n-v](https://github.com/mart1n-v)
## Features
Bot is in constant development and they may be new features or changes to the old ones.

Current commands:
- **.pcinfo** - Fetch information about the computer using the ```systeminfo``` command in command prompt.
- **.hardware** - Fetch information about the computer's hardware using WMIC. [GPU/CPU Name, HWID, RAM Capacity, Disk Capacity]
- **.shutdown** - Shutdown the computer.
- **.dir** - List the specified directory's files. Usage: ```.dir <full path>```
- **.tasklist** - List all tasks currently running on the host computer. Usage: ```.tasklist```
- **.taskkill** - Kill a specified task. Usage: ```.taskkill <PID>```
- **.screenshot** - Take a screenshot.
- **.open** - - Open a specified file. Usage: ```.open <full file path>```. Example: ```.open c:/Users/user/Desktop/textfile.txt```
- **.copy** - Copy a specified file. Usage: ```.copy <full file path>```. Example: ```.copy c:/Users/user/Desktop/textfile.txt```
- **.bsod** - Trigger a BSOD.
- **.changepassword** - Change the user's password. Usage: ```.changepassword <new password>```
- **.webcam** - Take a picture using the webcamera.
- **.logout** - Logout the user from the computer.
- **.delete** - Delete a specified file. Usage: ```.delete <full file path>```. Example: ```.delete c:/Users/user/Desktop/textfile.txt```
- **.upload** - Upload a file to the computer. Usage: ```.upload <full file path>```. You need to use the file that you want to upload as message attachment. Example: ```.upload c:/Users/user/Desktop/textfile.txt```
- **.hid** - Siumlates keyboard. Usage: ```.hid write <text>``` - writes text, ```.hid press <key>``` - simulates keypress, ```.hid hotkey <key1> <key2>``` - simulates keypresses of key1 and key2 at the same time.
            Examples: ```.hid write hello there``` - writes "hello there", ```.hid press enter``` - simulates keypress of enter key, ```.hid hotkey win r``` - simulates hotkey win + r.
- **.blockinput** - Block all input from the user's keyboard and mouse.
- **.unblockinput** - Unblock all input from the user's keyboard and mouse.
- **.selfdestruct** - Run a .bat file that removes the bot and all it's features from the computer.
- **.deletedir** - Delete a directory. Usage: ```.deletedir <full dir path>```. Example: ```.deletedir c:/Users/user/Desktop/MyFolder```
- **.createdir** - Create a directory. Usage: ```.createdir <new dir path>```. Example ```.createdir c:/Users/user/Desktop/MyNewFolder```
- **.modules** - List/run modules in the ```/modules``` folder. Usage: ```.modules <list/load> <if load, specify either file_name.py or "all">```
- **.clipboard** - Get/set the current clipboard item. Usage: ```.clipboard <get/set> <if you used ".clipboard set" parse the text to put into clipboard here>``` Note: ```.clipboard get``` returns the CURRENT copied text, not the whole history.
- **.networking** - Export ``ipconfig /all`` and send to discord.
- **.monitor** - Turn the infected machine's monitor on/off. Usage: ``.monitor <on/off>``
- **.cmd** - Emulates a cmd command. No output visible. Usage: ``.cmd <cmd>``
- **.pws** - Executes a powershell command. No output visible. ``.pws <cmd>``
- **.file_collector** - Run a file stealer wich collects ``.txt, .docx, .pdf, .csv`` files. If enabled in it's config, also collects ``.png, .jpg, .jpeg, .web`` files, however the size may exceed max discord limit.

This project supports custom modules. If you want to add your own script (not a command), create it and put it into the ```/modules``` folder. The bot runs these when launching itself. For reference see ```example_module.py``` in ```/modules```

## Instalation - User
- Create a new discord bot application at https://discord.com/developers/applications.
- Copy the token.
- Add the bot to a server where you'll use him.

- Download enc.py and paste the token into the "TOKEN_HERE" variable
- Copy the token (DO NOT COPY THE ``b'`` AT THE START AND THE ``'`` AT THE END.)
- Paste into the powershell code in the ``$property_value`` variable.


## Instalation - Host
The infection process is done through the use of some powershell code. You want them to run the .ps1 file and let it finish.

The powershell code will install Python 3.10.11, latest version of Snky and create a shortcut in the startup folder. Then it restarts the computer.

## Known Bugs
- None at the moment.

