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
subUrl = '/network/post-arp'

def getCommandResult():
    output = subprocess.getoutput("arp | awk '{print $1,$2,$3,$5}'").split('\n')
    del output[0]
    return output

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
    
def sendApiServer(nowTime, status, row):
    global subUrl
    tabs = row.split(' ')
    data = {'time': nowTime, 'status':status, 'address': tabs[0], 'hardwareType': tabs[1], 'hardwareAddress': tabs[2], 'interface': tabs[3]}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    ORIGINAL_DATAS = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in ORIGINAL_DATAS:
        if len(row.replace(' ', '')) > 0 :
            sendApiServer(nowTime, 'ORI', row)
    runThread()