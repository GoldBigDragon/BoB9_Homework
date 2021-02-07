# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

@author: GoldBigDragon
"""

import subprocess
import json
import threading
import main

global LASTNUM
LASTNUM = 0

global subUrl
subUrl = '/system/post-history'

def getCommandResult():
    output = subprocess.getoutput('./history.sh').split('\n')
    return output

def runThread():
    global LASTNUM
    lines = getCommandResult()
    for row in lines:
        splitted = row.split(' ')
        if int(splitted[0]) > LASTNUM and 'history' not in splitted[3]:
            sendApiServer(int(splitted[0]), splitted[1] + ' ' + splitted[2], ' '.join(splitted[3:]))
    lastnum = int(lines[-1].split(' ')[0])
    if lastnum > LASTNUM:
        LASTNUM = int(lines[-1].split(' ')[0])
    threading.Timer(5, runThread).start()

def sendApiServer(num, time, command):
    global subUrl
    data = {'num': num, 'time': time, 'command': command}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global LASTNUM
    subprocess.getoutput('export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "')
    f = open('history.sh', 'w')
    f.writelines("#!/bin/bash\n")
    f.writelines('export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "\n')
    f.writelines("HISTFILE=~/.bash_history\n")
    #f.writelines("HISTFILE=~/home/bob/.bash_history\n")
    f.writelines("set -o history\n")
    f.writelines("history | tail -n 100 | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16}'")
    f.close()
    subprocess.getoutput('chmod +x history.sh')
    histories = getCommandResult()
    for row in histories:
        splitted = row.split(' ')
        if int(splitted[0]) > LASTNUM and 'history' not in splitted[3]:
            sendApiServer(int(splitted[0]), splitted[1] + ' ' + splitted[2], ' '.join(splitted[3:]))
    if len(histories) > 0 :
        LASTNUM = int(histories[-1].split(' ')[0])
    runThread()