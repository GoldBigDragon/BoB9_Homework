# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: GoldBigDragon
"""
import subprocess
import json
import threading
from datetime import datetime

import main

global internetSubUrl
global socketSubUrl
internetSubUrl = '/network/post-conn'
socketSubUrl = '/network/post-socks'

global INTERNET_ORIGINAL_DATAS
INTERNET_ORIGINAL_DATAS = []

global SOCKET_ORIGINAL_DATAS
SOCKET_ORIGINAL_DATAS = []

global inited
inited = False

global INTERNET_DATAS
INTERNET_DATAS = []
global SOCKET_DATAS
SOCKET_DATAS = []
def getCommandResult():
    output = subprocess.getoutput("netstat -naop | awk '{print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10}'").split('\n')
    return output

def runThread():
    global inited
    global INTERNET_DATAS
    global SOCKET_DATAS
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output =  getCommandResult()
    isSocket = False
    for row in output:
        if('(Not all processes could be identified, non-owned process info' in row or
           ' will not be shown, you would have to be root to see it all.)' in row or 
           'Active Internet connections (servers and established)' in row or
           'Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name' in row or
           'Active UNIX domain sockets (servers and established)' in row or
           'DGRAM' in row):
            continue
        if('Proto RefCnt Flags Type State I-Node PID/Program name Path' in row):
            isSocket = True
            continue
        sendApiServer(nowTime, isSocket, row)
    inited = True
    removedInternetDatas = list(set(INTERNET_ORIGINAL_DATAS) - set(INTERNET_DATAS))
    removedSocketDatas = list(set(SOCKET_ORIGINAL_DATAS) - set(SOCKET_DATAS))
    for row in removedInternetDatas:
        sendApiServer(nowTime, False, row)
        INTERNET_ORIGINAL_DATAS.remove(row)
    for row in removedSocketDatas:
        sendApiServer(nowTime, True, row)
        SOCKET_ORIGINAL_DATAS.remove(row)
    INTERNET_DATAS.clear()
    SOCKET_DATAS.clear()
    threading.Timer(10, runThread).start()

def sendApiServer(nowTime, isSocket, row):
    global internetSubUrl
    global socketSubUrl
    global INTERNET_ORIGINAL_DATAS
    global SOCKET_ORIGINAL_DATAS
    global inited
    global INTERNET_DATAS
    global SOCKET_DATAS
    
    row = row.replace('[ ]', '[ x ]').replace('  ', ' ').replace('off ', 'off').replace('timewait ', 'timewait')
    tabs = row.split(' ')
    data = None
    pid = -1
    programName = None
    status = 'ADD'
    if inited == False:
        status = 'ORI'
    if isSocket == True:
        if len(tabs) == 10 :
            SOCKET_DATAS.append(row)
            if(row not in SOCKET_ORIGINAL_DATAS):
                SOCKET_ORIGINAL_DATAS.append(row)
                if '/' in tabs[8]:
                    pid = int(tabs[8].split('/')[0])
                    programName = '/'.join(tabs[8].split('/')[1:])
                data = {'time': nowTime, 'status':status, 'proto': tabs[0], 'refCnt': int(tabs[1]), 'type': tabs[5], 'state': tabs[6], 'iNode': int(tabs[7]), 'pid': pid, 'programName': programName, 'path': tabs[9]}
                main.serverSender(socketSubUrl, json.dumps(data))
    else :
        INTERNET_DATAS.append(row)
        if(row not in INTERNET_ORIGINAL_DATAS):
            INTERNET_ORIGINAL_DATAS.append(row)
            if len(tabs) >= 9:
                if '/' in tabs[6]:
                    pid = int(tabs[6].split('/')[0])
                    programName = '/'.join(tabs[6].split('/')[1:])
                if tabs[5] == "TIME_WAIT":
                    return
                data = {'time': nowTime, 'status':status, 'proto': tabs[0], 'localAddress': tabs[3], 'foreignAddress': tabs[4], 'state': tabs[5], 'pid': pid, 'programName': programName, 'timer': tabs[7]}
            else :
                if '/' in tabs[5]:
                    pid = int(tabs[5].split('/')[0])
                    programName = '/'.join(tabs[5].split('/')[1:])
                data = {'time': nowTime, 'status':status, 'proto': tabs[0], 'localAddress': tabs[3], 'foreignAddress': tabs[4], 'state': None, 'pid': pid, 'programName': programName, 'timer': tabs[6]}
            main.serverSender(internetSubUrl, json.dumps(data))

def sendApiServerDel(nowTime, isSocket, row):
    global internetSubUrl
    global socketSubUrl
    row = row.replace('[', '').replace(']', '').replace('  ', ' ').replace('off ', 'off').replace('timewait ', 'timewait')
    tabs = row.split(' ')
    data = None
    pid = -1
    programName = None
    if isSocket == True:
        if len(tabs) == 10 :
            if '/' in tabs[8]:
                pid = int(tabs[8].split('/')[0])
                programName = '/'.join(tabs[8].split('/')[1:])
            data = {'time': nowTime, 'status': "DEL", 'proto': tabs[0], 'refCnt': int(tabs[1]), 'type': tabs[5], 'state': tabs[6], 'iNode': int(tabs[7]), 'pid': pid, 'programName': programName, 'path': tabs[9]}
            main.serverSender(socketSubUrl, json.dumps(data))
    else :
        if len(tabs) >= 9:
            if '/' in tabs[6]:
                pid = int(tabs[6].split('/')[0])
                programName = '/'.join(tabs[6].split('/')[1:])
            data = {'time': nowTime, 'status': "DEL", 'proto': tabs[0], 'localAddress': tabs[3], 'foreignAddress': tabs[4], 'state': tabs[5], 'pid': pid, 'programName': programName, 'timer': tabs[7]}
        else :
            if '/' in tabs[5]:
                pid = int(tabs[5].split('/')[0])
                programName = '/'.join(tabs[5].split('/')[1:])
            data = {'time': nowTime, 'status': "DEL", 'proto': tabs[0], 'localAddress': tabs[3], 'foreignAddress': tabs[4], 'state': None, 'pid': pid, 'programName': programName, 'timer': tabs[6]}
        main.serverSender(internetSubUrl, json.dumps(data))

def start():
    runThread()