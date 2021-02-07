# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: 조서연, GoldBigDragon
"""

import subprocess
import json
import main
import socket
from datetime import datetime
from requests import get

global subUrl
subUrl = '/system/post-info'

def getCommandResult(command):
    results = subprocess.getoutput(command)
    return results

def sendApiServer():
    global subUrl
    results = getCommandResult('cat /proc/version')
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    externalIp = get('https://api.ipify.org').text
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIp = s.getsockname()[0]
    data = {'time': nowTime, 'externalIp':externalIp, 'localIp':localIp, 'systemVersion': results}
    main.serverSender(subUrl, json.dumps(data))

def start():
    sendApiServer()