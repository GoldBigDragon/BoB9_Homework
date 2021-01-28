# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: 조서연, GoldBigDragon
"""

import subprocess
import requests
import json
import threading
import main

global subUrl
subUrl = '/system/post-time'

def getCommandResult(command):
    results = subprocess.getoutput(command)
    return results

def runThread():
    results = getCommandResult('date "+%Y-%m-%d %H:%M:%S"')
    sendApiServer(results)
    threading.Timer(5, runThread).start()

def sendApiServer(row):
    global subUrl
    data = {'systemTime': row}
    try:
        requests.post(main.serverAddress + subUrl, data=json.dumps(data), timeout=60)
    except Exception:
        pass

def start():
    runThread()