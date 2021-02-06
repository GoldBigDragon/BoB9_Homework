# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:16:22 2021

@author: GoldBigDragon
"""

import subprocess
import json
from datetime import datetime
import threading
import random

import main

global subUrl
subUrl = '/attack/network/post-log'

global moduleName
moduleName = 'PortOpener'

def runCommand():
    port = random.randrange(1,65535)
    subprocess.getoutput("sudo iptables -I INPUT 1 -p tcp --dport " + str(port) + " -j ACCEPT")
    subprocess.getoutput("sudo iptables -I INPUT 1 -p tcp --sport " + str(port) + " -j ACCEPT")
    return "Port " + str(port) + " was open."

def runThread():
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = runCommand()
    sendApiServer(nowTime, message)
    threading.Timer(10, runThread).start()

def sendApiServer(time, message):
    global subUrl
    global moduleName
    data = {'time': time, 'type': moduleName, 'message': message}
    main.serverSender(subUrl, json.dumps(data))

def start():
    runThread()