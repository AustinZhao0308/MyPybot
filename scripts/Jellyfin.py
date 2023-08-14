import os, subprocess
import signal
import psutil
import time
from PyOfficeRobot.core.WeChatType import *
import PyOfficeRobot

jf_process = None

def close_program(program_name):
    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['pid', 'name'])
            if program_name.lower() in process_info['name'].lower():
                pid = process_info['pid']
                process = psutil.Process(pid)
                process.terminate()
                print(f"Closed {process_info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def startServer():
    PyOfficeRobot.chat.send_message("akinaustin", "Starting jellyfin...")
    path = "C:/Users/Lenovo/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/jellyfin.lnk"
    subprocess.call(["start", "", path], shell=True)


def killServer():
    PyOfficeRobot.chat.send_message("akinaustin", "Closing jellyfin...")
    close_program("jellyfin.exe")
