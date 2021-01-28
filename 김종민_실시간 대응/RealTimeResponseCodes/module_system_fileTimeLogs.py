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

global ORIGINAL_DATAS
ORIGINAL_DATAS = []

global subUrl
subUrl = '/system/post-file'
    
def getCommandResult():
    results = []
    output = subprocess.getoutput("ls /bin/ --time-style='+%Y-%m-%d %H:%M:%S' -alt 2> /dev/null | grep x").split('\n')
    for row in output:
        results.append(row.replace('  ', ' '))
    return results

def runThread():
    global ORIGINAL_DATAS
    results =  getCommandResult()
    if (results != ORIGINAL_DATAS):
        for row in results:
            if row not in ORIGINAL_DATAS:
                sendApiServer(row)
                ORIGINAL_DATAS.append(row)
    threading.Timer(5, runThread).start()

def sendApiServer(row):
    global subUrl
    tabs = row.split(' ')
    for i in range(5):
        if '' in tabs:
            tabs.remove('')
    time = tabs[5] + ' ' + tabs[6]
    if tabs[7] != '.':
        data = {'time': time, 'permission': tabs[0], 'user': tabs[2], 'userGroup': tabs[3], 'size':tabs[4], 'filePath': tabs[7]}
        try:
            requests.post(main.serverAddress + subUrl, data=json.dumps(data), timeout=60)
        except Exception:
            pass

def start():
    global ORIGINAL_DATAS
    ORIGINAL_DATAS = getCommandResult()
    runThread()