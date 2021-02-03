# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

@author: 백승훈, GoldBigDragon
"""

import subprocess
import json
from dateutil.parser import parse
import threading
import main

global ORIGINAL_DATAS
ORIGINAL_DATAS = []

global subUrl
subUrl = '/system/post-web'

def getCommandResult():
    output = subprocess.getoutput("cat 찾은 액세스로그 파일 경로").split('\n')
    parsedline = [] # [날짜, 메소드(GET/POST), user, 메시지, 데이터 크기(없으면 0)]
    result = []
    for row in output:
        tabs = row.split(' ')
        if (len(tabs) < 3):
            return result
        datetmp = tabs[3][1:]
        dateindex = datetmp.find(':')
        datetmp = datetmp[:dateindex] + ' ' + datetmp[dateindex+1:]
        parsedline.append(parse(datetmp).strftime('%Y-%m-%d %X'))
        parsedline.append(tabs[5][1:])
        parsedline.append(tabs[0])
        message = ''
        for i in range(6, len(tabs)):
            message += tabs[i] + ' '
        parsedline.append(message)
        result.append(parsedline)
        parsedline = []
    return result

def runThread():
    global ORIGINAL_DATAS
    output = getCommandResult()
    if (output != ORIGINAL_DATAS):
        for log in output:
            if log not in ORIGINAL_DATAS:
                sendApiServer('ADD', log)
                ORIGINAL_DATAS.append(log)
    threading.Timer(5, runThread).start()

def sendApiServer(status, log):
    global subUrl
    data = {'time': log[0], 'status':status, 'method': log[1], 'user': log[2], 'message': log[3], 'size': log[4]}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    output = getCommandResult()
    for log in output:
        sendApiServer('ORI', log)
    ORIGINAL_DATAS = output
    runThread()