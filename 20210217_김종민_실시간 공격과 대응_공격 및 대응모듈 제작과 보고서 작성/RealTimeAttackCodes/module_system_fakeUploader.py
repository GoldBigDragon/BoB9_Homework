# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:38:56 2021

@author: GoldBigDragon
"""

import subprocess
import json
from datetime import datetime
import threading
import random

import module_util_trick
import main

global subUrl
subUrl = '/attack/post-createFile'

global moduleName
moduleName = 'FakeFileCreator'

def runCommand():
    dirName = module_util_trick.getRandomChar(32)
    fileName = module_util_trick.getRandomChar(32) + '.sh'
    subprocess.getoutput('echo user | sudo -S mkdir /var/www/html/board_file/' + dirName)
    subprocess.getoutput('echo user | sudo -S chown www-data:www-data /var/www/html/board_file/' + dirName)
    subprocess.getoutput('echo user | sudo -S chmod 777 /var/www/html/board_file/' + dirName)
    subprocess.getoutput('echo user | sudo -S echo "' + fakeShellCodeGenerator() + '" > /var/www/html/board_file/' + dirName + '/' + fileName)
    subprocess.getoutput('echo user | sudo -S chmod 755 /var/www/html/board_file/' + dirName)
    return dirName, fileName

def runThread():
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dirName, fileName = runCommand()
    sendApiServer(nowTime, dirName, fileName)
    if main.start:
        threading.Timer(random.randint(0, 10), runThread).start()

def fakeShellCodeGenerator():
    returnString = ''
    for i in range(random.randint(1, 25)):
        randomFunction = random.randint(0, 10)
        if randomFunction % 7 == 0:
            returnString += 'sudo '
        if randomFunction == 0:
            returnString += 'cd ' + module_util_trick.getRandomDirectory()
        elif randomFunction == 1:
            returnString += './' + module_util_trick.getRandomName(module_util_trick.getRandomExtension())
        elif randomFunction == 2:
            returnString += 'chmod 777 ./' + module_util_trick.getRandomName(module_util_trick.getRandomExtension())
        elif randomFunction == 3:
            returnString += 'chmod 755 ./' + module_util_trick.getRandomName(module_util_trick.getRandomExtension())
        elif randomFunction == 4:
            returnString += 'mkdir ' + module_util_trick.getRandomDirectoryName()
        elif randomFunction == 5:
            returnString += 'rmdir ' + module_util_trick.getRandomDirectoryName()
        elif randomFunction == 6:
            returnString += 'rm ' + module_util_trick.getRandomName(module_util_trick.getRandomExtension())
        elif randomFunction == 7:
            returnString += module_util_trick.getRandomCommand()
        else:
            returnString += 'echo "' + module_util_trick.getRandomHex() + '" > ' + module_util_trick.getRandomName(module_util_trick.getRandomExtension())
        returnString += '\n'
    return returnString

def sendApiServer(time, directoryName, fileName):
    global subUrl
    global moduleName
    data = {'time': time, 'status': 'ADD', 'directoryName': '/var/www/html/board_file/'+directoryName, 'fileName': fileName}
    main.serverSender(subUrl, json.dumps(data))
    data = {'time': time, 'type': moduleName, 'message': "File '" + directoryName+'/'+fileName + "' was created."}
    main.serverSender('/attack/post-log', json.dumps(data))

def start():
    runThread()