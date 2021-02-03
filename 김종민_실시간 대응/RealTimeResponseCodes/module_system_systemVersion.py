# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: 조서연, GoldBigDragon
"""

import subprocess
import json
import main
from datetime import datetime

global subUrl
subUrl = '/system/post-info'

def getCommandResult(command):
    results = subprocess.getoutput(command)
    return results

def sendApiServer():
    global subUrl
    results = getCommandResult('cat /proc/version')
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': nowTime, 'systemVersion': results}
    main.serverSender(subUrl, json.dumps(data))

def start():
    sendApiServer()