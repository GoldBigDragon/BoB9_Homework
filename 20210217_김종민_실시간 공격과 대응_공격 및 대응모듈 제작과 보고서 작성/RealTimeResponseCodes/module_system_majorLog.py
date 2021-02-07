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

global target
target = [
    [0, "/var/log/auth.log", "cat /var/log/auth.log | tail -n 100"],
    [1, "/var/log/wtmp", "last -F | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25}'"],
    [2, '/var/log/messages.log', "cat /var/log/messages | tail -n 100"],
    [3, '/var/log/cron.log', "cat /var/log/cron.log | tail -n 100 | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25}"],
    [4, '/var/log/vsftpd.log', "cat /var/log/vsftpd.log | tail -n 100 | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25}"]
    ]

global subUrl
subUrl = '/system/post-major'

global inited
inited = []

def runThread():
    global ORIGINAL_DATAS
    global target
    global inited
    for t in target:
        targetNumber = t[0]
        lines = subprocess.getoutput(t[2]).split('\n')
        if len(lines) > 1 :
            for row in lines:
                tabs = row.split(' ')
                if len(row.replace(' ', '')) < 2:
                    continue
                tabs = [i for i in tabs if i != '']
                now = ''
                user = ''
                message = ''
                if (len(tabs) > 3):
                    # auth
                    if targetNumber == 0:
                        now = getTime(tabs[0] + ' ' + tabs[1] + ' ' + tabs[2] + ' 2021')
                        user = tabs[4] + ' ' + tabs[5]
                        message = ' '.join(tabs[6:])
                    # wtmp
                    elif targetNumber == 1 and 'wtmp begins' not in row:
                        user = tabs[0]
                        if 'reboot system' in row:
                            now = getTime(' '.join(tabs[4:8]))
                            message = ' '.join(tabs[15:])
                        else:
                            now = getTime(' '.join(tabs[3:7]))
                            message = ' '.join(tabs[9:])
                    # messages, cron
                    elif targetNumber == 2 or targetNumber == 3:
                        now = getTime(tabs[0] + ' ' + tabs[1] + ' ' + tabs[2] + ' 2021')
                        user = tabs[4]
                        message = ' '.join(tabs[5:])
                    # vsftpd
                    elif targetNumber == 4:
                        now = getTime(tabs[0] + ' ' + tabs[1] + ' ' + tabs[2] + ' ' + tabs[3] + ' ' + tabs[4])
                        user = tabs[6]
                        if tabs[11] == 'o':
                            message += 'output '
                        elif tabs[11] == 'i':
                            message += 'input '
                        message += 'data path:' + tabs[8]
                        message += ' with account(' + tabs[13] + ')'
                        if tabs[17] == 'c':
                            message += ' completed'
                        elif tabs[17] == 'i':
                            message += ' incomplete'
                    if now == None or message == None or user == None or len(message) < 2 or len(user) < 2:
                        continue
                    if inited[targetNumber] == False:
                        sendApiServer(now, 'ORI', target[targetNumber][1], user, message)
                        ORIGINAL_DATAS[targetNumber].append(now+target[targetNumber][1]+user+message)
                    elif now+target[targetNumber][1]+user+message not in ORIGINAL_DATAS[targetNumber]:
                        sendApiServer(now, 'ADD', target[targetNumber][1], user, message)
                        ORIGINAL_DATAS[targetNumber].append(now+target[targetNumber][1]+user+message)
        if inited[targetNumber] == False:
            inited[targetNumber] = True
    threading.Timer(5, runThread).start()

def getTime(timeString):
    try :
        return parse(timeString).strftime('%Y-%m-%d %X')
    except Exception:
        return None

def sendApiServer(time, status, path, user, message):
    global subUrl
    data = {'time': time, 'status':status, 'path': path, 'user': user, 'message': message}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    global target
    global inited
    for t in target:
        ORIGINAL_DATAS.append([])
        inited.append(False)
    runThread()