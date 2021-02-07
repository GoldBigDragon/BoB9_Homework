# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:42:36 2021

@author: GoldBigDragon
"""

import subprocess
import json
from datetime import datetime
import threading

import module_util_trick
import main

global subUrl
subUrl = '/attack/post-log'

global moduleName
moduleName = 'FakeProcessGenerator'

def createPythonScript():
    dirName = module_util_trick.getRandomDirectory()
    fileName = module_util_trick.getRandomName('py')
    pythonScript = module_util_trick.getRandomPythonScript()
    subprocess.getoutput('echo user | sudo -S chmod 777 ' + dirName)
    subprocess.getoutput('echo user | sudo -S echo "' + pythonScript[1] + '" > ' + dirName + '/' + fileName)
    subprocess.getoutput('echo user | sudo -S chmod 755 ' + dirName)
    return dirName, fileName, pythonScript[0]

def runThread():
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dirName, fileName, pythonScript = createPythonScript()
    sendApiServer(nowTime, dirName, fileName, pythonScript)
    subprocess.getoutput('echo user | sudo -S python3 ' + dirName+'/'+fileName)
    if main.start:
        threading.Timer(5, runThread).start()

def sendApiServer(time, dirName, fileName, pythonScript):
    global subUrl
    global moduleName
    data = {'time': time, 'type': moduleName, 'message': 'Run python script about "' + pythonScript + '" from "' + dirName+"/"+fileName +'"'}
    main.serverSender(subUrl, json.dumps(data))
    data = {'time': time, 'status': 'ADD', 'directoryName': dirName, 'fileName': fileName}
    main.serverSender('/attack/post-createFile', json.dumps(data))

def start():
    runThread()