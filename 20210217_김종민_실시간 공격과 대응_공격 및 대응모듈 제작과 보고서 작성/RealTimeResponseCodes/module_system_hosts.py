# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

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
subUrl = '/system/post-hosts'

def getCommandResult():
    results = []
    output = subprocess.getoutput("cat /etc/hosts | awk '{print $1, $2}'").split('\n')
    for row in output:
        if '#' not in row and len(row.replace(' ', '')) > 0:
            results.append(row)
    return results

def runThread():
    global ORIGINAL_DATAS
    results = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in results:
        if row not in ORIGINAL_DATAS:
            sendApiServer(nowTime, 'ADD', row)
            ORIGINAL_DATAS.append(row)
    removedDatas = list(set(ORIGINAL_DATAS) - set(results))
    for row in removedDatas:
        sendApiServer(nowTime, 'DEL', row)
        ORIGINAL_DATAS.remove(row)
    threading.Timer(10, runThread).start()

def sendApiServer(nowTime, status, address):
    global subUrl
    data = {'time': nowTime, 'status': status, 'address': address}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    ORIGINAL_DATAS = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in ORIGINAL_DATAS:
        if len(row.replace(' ', '')) > 0 :
            sendApiServer(nowTime, 'ORI', row)
    runThread()