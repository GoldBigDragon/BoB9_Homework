# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: GoldBigDragon
"""

import subprocess
import json
from datetime import datetime
import threading
import main

global ORIGINAL_DATAS
ORIGINAL_DATAS = []

global subUrl
subUrl = '/system/post-passwd'

def getCommandResult():
    results = []
    output = subprocess.getoutput("cat /etc/passwd").split('\n')
    for row in output:
        results.append(row)
    return results

def runThread():
    global ORIGINAL_DATAS
    results = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if (results != ORIGINAL_DATAS):
        for row in results:
            if row not in ORIGINAL_DATAS:
                sendApiServer(nowTime, 'ADD', row)
                ORIGINAL_DATAS.append(row)
        removedDatas = list(set(ORIGINAL_DATAS) - set(results))
        for row in removedDatas:
            sendApiServer(nowTime, 'DEL', row)
            ORIGINAL_DATAS.remove(row)
    threading.Timer(10, runThread).start()

def sendApiServer(nowTime, status, row):
    global subUrl
    tabs = row.split(':')
    data = {'time': nowTime, 'status': status, 'user': tabs[0], 'uid':int(tabs[2]), 'gid':int(tabs[3]), 'name':tabs[4], 'homeDir':tabs[5], 'loginShell':tabs[6]}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    ORIGINAL_DATAS = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in ORIGINAL_DATAS:
        sendApiServer(nowTime, 'ORI', row)
    runThread()