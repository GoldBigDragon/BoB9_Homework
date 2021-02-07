# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:13 2021

@author: GoldBigDragon
"""

import requests
import json
import threading
import main
import os

def getFiles(directory):
    fileList = []
    try:
        for file in os.listdir(directory):
            if os.path.isfile(directory+file):
                fileList.append(directory+file)
            elif (os.path.isdir(directory+file)):
                fileList.extend(getFiles(directory+file+"/"))
    except:
        pass
    return fileList

def getTargetFiles():
    url = main.serverAddress+'/file/getTarget'
    try:
        return requests.get(url, timeout=60).json()
    except Exception:
        return None

def uploadFile(filepath):
    try:
        files = {'filetoupload':open(filepath,'rb')}
        requests.get(main.serverAddress + '/fileupload', files=files, timeout=10)
    except Exception as E:
        print('UPLOAD ERROR : ', E)
        pass

def runThread():
    output = getTargetFiles()
    if output != None:
        for row in output:
            if row["isDir"] == 0:
                uploadFile(row["filePath"])
            else:
                dirPath = row["filePath"]
                if dirPath[-1] != '/':
                    dirPath += '/'
                for file in getFiles(dirPath):
                    uploadFile(file)
            main.serverSender('/file/updateTarget', json.dumps({'id': row["id"]}))
    threading.Timer(5, runThread).start()

def start():
    runThread()