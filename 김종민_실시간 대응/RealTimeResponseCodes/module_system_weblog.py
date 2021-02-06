# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

@author: GoldBigDragon
"""

from datetime import datetime
import subprocess
import json
import threading
import main

global LAST_TIME_STAMP
LAST_TIME_STAMP = 0

global subUrl
subUrl = '/system/post-web'

def getCommandResult():
    output = subprocess.getoutput("cat /var/log/apache2/access.log | tail -n 200").split('\n')
    return output

def runThread():
    global LAST_TIME_STAMP
    output = getCommandResult()
    lastTimeStamp = 0
    for row in output:
        tabs = row.split(' ')
        if (len(tabs) < 11):
            continue
        time = datetime.strptime(tabs[3].replace("[", ""), '%d/%b/%Y:%X')
        nowTimeStamp = time.timestamp()
        if LAST_TIME_STAMP - nowTimeStamp < 0:
            ip = tabs[0]
            method = tabs[5].replace('"', '')
            param = tabs[6]
            ssl = tabs[7].replace('"', '')
            code = int(tabs[8])
            size = int(tabs[9])
            path = tabs[10].replace('"', '')
            datas = ' '.join(tabs[11:])
            sendApiServer(time.strftime('%Y-%m-%d %X'), ip, method, param, ssl, code, size, path, datas)
            lastTimeStamp = nowTimeStamp
    LAST_TIME_STAMP = lastTimeStamp
    threading.Timer(5, runThread).start()

def sendApiServer(time, ip, method, param, ssl, code, size, path, datas):
    global subUrl
    data = {'time': time, 'ip': ip, 'method': method, 'param': param, 'ssl': ssl, 'code': code, 'size':size, 'path':path, 'datas':datas}
    main.serverSender(subUrl, json.dumps(data))

def start():
    if '그런 파일이나 디렉터리가 없습니다' not in subprocess.getoutput("cat /var/log/apache2/access.log"):
        runThread()