# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: 백승훈, GoldBigDragon
"""
import subprocess
import json
import threading
from datetime import datetime

import main

global ORIGINAL_DATAS
ORIGINAL_DATAS = []

global subUrl
subUrl = '/process/post-lsmod'

def getCommandResult():
    results = subprocess.getoutput("lsmod | awk '{print $1, $2, $3, $4}'").split('\n')
    del results[0]
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
    threading.Timer(5, runThread).start()

def sendApiServer(time, status, row):
    global subUrl
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tabs = row.split(' ')
    if len(tabs) > 3:
        data = {'time': nowTime, 'status': status, 'name': tabs[0], 'size': int(tabs[1]), 'used': int(tabs[2]), 'daemon': tabs[3]}
    else :
        data = {'time': nowTime, 'status': status, 'name': tabs[0], 'size': int(tabs[1]), 'used': int(tabs[2]), 'daemon': None}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    ORIGINAL_DATAS = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in ORIGINAL_DATAS:
        sendApiServer(nowTime, 'ORI', row)
    runThread()