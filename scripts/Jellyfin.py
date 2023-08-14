import os, subprocess
import signal
import time
jf_process = None

def startServer():
    global jf_process
    if jf_process is not None and jf_process.poll() is None:
        jf_process.send_signal(signal.CTRL_BREAK_EVENT)
        jf_process.wait()

    subprocess.Popen("D:\\Program Files\\jellyfin_10.8.9\\jellyfin.exe")

def killServer():
    global jf_process
    if jf_process is not None and jf_process.poll() is None:
        jf_process.send_signal(signal.CTRL_BREAK_EVENT)
        jf_process.wait()
        jf_process = None
