# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 06:21:26 2021

@author: GoldBigDragon
"""

import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

global suspectPid
global suspectStruct
suspectPid = []
suspectStruct = []

def getResult(subUrl, startTime, endTime):
    html = urlopen("http://localhost:3123/"+subUrl+"?startTime="+startTime+"&endTime="+endTime)
    bsObject = BeautifulSoup(html, "html.parser")
    return json.loads(bsObject.text)

def addSuspectData(pid, data):
    global suspectStruct
    for i in range(len(suspectStruct)):
        if suspectStruct[i][0] == pid:
            suspectStruct[i][1] = suspectStruct[i][1] + list(data.items())
            break

def getData(subUrl, startTime, endTime):
    global suspectPid
    tempPid = []
    socketConnection = getResult(subUrl, "2021-01-01", "2022-01-01")
    for entry in socketConnection:
        if entry['pid'] in suspectPid:
            if entry["pid"] not in tempPid:
                tempPid.append(entry['pid'])
                addSuspectData(entry['pid'], entry)

if __name__ == '__main__':
    internetConnection = getResult("network/get-internet", "2021-01-01", "2022-01-01")
    for entry in internetConnection:
        if (entry['state'] == 'LISTEN' or entry['state'] == 'ESTABLISHED') and entry["localAddress"].split(":")[0].split(".")[0] != '127' and (entry["foreignAddress"].split(":")[-1] == "*" or int(entry["foreignAddress"].split(":")[-1]) > 1000):
            if entry["pid"] not in suspectPid:
                suspectPid.append(entry['pid'])
                suspectStruct.append([entry['pid'], list(entry.items())])
    getData("network/get-socket", "2021-01-01", "2022-01-01")
    getData("process/get-lsof", "2021-01-01", "2022-01-01")
    getData("process/get-status", "2021-01-01", "2022-01-01")
    for suspect in suspectStruct:
        print("*****[PID - "+str(suspect[0])+"]*****")
        print(suspect)