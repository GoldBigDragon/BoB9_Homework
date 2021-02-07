# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

@author: 백승훈, GoldBigDragon
"""

import subprocess
import json
from datetime import datetime
from dateutil.parser import parse
import threading
import hashlib
import main

global subUrl
subUrl = '/system/post-rootkit'

global ORIGINAL_COMMANDS
ORIGINAL_COMMANDS = {}
global ORIGINAL_CMD_HASHTABLE
ORIGINAL_CMD_HASHTABLE = {}
global Checked_Commands
Checked_Commands = ['lastlog', 'basename', 'chfn', 'chsh', 'crontab', 'du', 'dirname', 'env', 'find', 'sudo', 'killall', 'lsof', 'passwd', 'pstree', 'slogin', 'top', 'w', 'write']

def backupcommands():
    for cmd in Checked_Commands:
        path = '/usr/bin/' + cmd
        try :
            with open(path, 'rb') as f:
                bytestr = f.read()
                ORIGINAL_COMMANDS[cmd] = bytestr
                ORIGINAL_CMD_HASHTABLE[cmd] = hashlib.md5(bytestr).hexdigest()
                f.close()
        except Exception:
            pass

def runThread():
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for cmd in Checked_Commands:
        path = '/usr/bin/' + cmd
        with open(path, 'rb') as f:
            bytestr = f.read()
            if ORIGINAL_CMD_HASHTABLE[cmd] != hashlib.md5(bytestr).hexdigest(): # 명령어 파일 변조 확인
                date = subprocess.getoutput("date -r " + path)
                modifiedTime = parse(date).strftime('%Y-%m-%d %X')
                sendApiServer(nowTime, path, modifiedTime)
                f.close()
                with open(path, 'wb') as f:
                    f.write(ORIGINAL_COMMANDS[cmd]) # 원본 복구
                    f.close()
            else:
                continue
    threading.Timer(5, runThread).start()

def sendApiServer(nowTime, path, modifiedTime):
    global subUrl
    data = {'time': nowTime, 'path': path, 'modifiedTime': modifiedTime}
    main.serverSender(subUrl, json.dumps(data))

def start():
    backupcommands()
    runThread()