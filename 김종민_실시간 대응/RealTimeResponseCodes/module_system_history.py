# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

@author: GoldBigDragon
"""

import subprocess
import requests
import json
from datetime import datetime
import threading
import main

import pymysql

global LASTNUM
LASTNUM = 0

global subUrl
subUrl = '/system/post-history'

def runCommand(command):
    output = subprocess.getoutput(command)
    return output

def getNow():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def getHistory():
    output = runCommand("./history.sh")
    lines = output.split('\n')
    print(lines)
    return lines

def runThread():
    global LASTNUM
    print('Running...')
    lines = getHistory()
    for row in lines:
        splitted = row.split(' ')
        if int(splitted[0]) > LASTNUM and 'history' not in splitted[2]:
            sendApiServer(int(splitted[0]), splitted[1].replace('_', ' '), ' '.join(splitted[2:]))
            #insertMySQL(int(splitted[0]), splitted[1].replace('_', ' '), ' '.join(splitted[2:]))
    LASTNUM = int(lines[-1].split(' ')[0])
    threading.Timer(5, runThread).start()

def sendApiServer(num, time, command):
    global subUrl
    data = {'num': num, 'time': time, 'command': command}
    try:
        requests.post(main.serverAddress + subUrl, data=json.dumps(data), timeout=60)
    except requests.exceptions.Timeout:
        print('Time out')

def insertMySQL(num, time, command):
    conn = pymysql.connect(host='localhost', user='root', password='root', db='realtimeResponse', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO `realtimeResponse`.`history` (num, time, command) VALUES(%s, %s, %s);"
    cursor.execute(sql,(num, time, command, ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    subprocess.getoutput('export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "')
    f = open('history.sh', 'w')
    f.writelines("#!/bin/bash\n")
    f.writelines("HISTFILE=~/.bash_history\n")
    #f.writelines("HISTFILE=~/home/bob/.bash_history\n")
    f.writelines("set -o history\n")
    f.writelines("history | tail -n 100 | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16}'")
    f.close()
    subprocess.getoutput('chmod +x history.sh')
    histories = getHistory()
    if len(histories) > 0 :
        LASTNUM = int(getHistory()[-1].split(' ')[0])
    runThread()