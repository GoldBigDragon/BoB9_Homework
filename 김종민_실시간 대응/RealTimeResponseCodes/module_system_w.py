# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: GoldBigDragon
"""

import subprocess
import json
import threading
import main
from datetime import datetime

global subUrl
subUrl = '/system/post-w'

def getCommandResult():
    results = []
    uptime = None
    users = 0
    output = subprocess.getoutput("w | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15}'").split('\n')
    for row in output:
        if 'up' in row and 'user' in row and 'load average' in row:
            splitted = row.split(',')
            uptime = splitted[0].replace(' ', '')
            users = int(splitted[1].split('user')[0].replace(' ', ''))
        elif 'USER' not in row and 'TTY' not in row and 'FROM' not in row and 'LOGIN@' not in row:
            results.append(row)
    return uptime, users, results

def runThread():
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    uptime, users, results =  getCommandResult()
    for row in results:
        sendApiServer(nowTime, uptime, users, row)
    threading.Timer(5, runThread).start()

def sendApiServer(nowTime, uptime, users, row):
    global subUrl
    tabs = row.split(' ')
    data = {'time':nowTime, 'upTime': uptime, 'loginUsers': users, 'user':tabs[0], 'tty': tabs[1], 'connectFrom': tabs[2], 'loginTime': tabs[3], 'what': ' '.join(tabs[7:])}
    main.serverSender(subUrl, json.dumps(data))

def start():
    runThread()