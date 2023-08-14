import os
from os import system

def ShutdownComputer():
    os.system("shutdown -s -t  60 ")

def RestartComputer():
    system("shutdown -r -t 100")