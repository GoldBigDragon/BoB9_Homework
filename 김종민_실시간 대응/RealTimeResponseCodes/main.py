# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:52:06 2021

@author: GoldBigDragon
"""

import requests
import threading
import json
import sys

import module_network_arp
import module_network_netstat
import module_network_packetSniffer
import module_process_status
import module_process_lsof
import module_process_lsmod
import module_system_fileTimeLogs
import module_system_hosts
import module_system_systemTime
import module_system_password
import module_system_systemVersion
import module_system_w
import module_system_lastlog
import module_system_history
import module_system_weblog
import module_system_majorLog
import module_system_rootkit
import module_etc_file

global serverAddress
serverAddress = 'http://112.148.181.37:3123'

def serverSender(subUrl, data):
    global serverAddress
    # binary
    # Don't remove front of 'b'
    hexData = {'data':  "b"+"".join("{:02x}".format(ord(c)) for c in data[::-1])}
    try:
        requests.post(serverAddress + subUrl, data=json.dumps(hexData), timeout=60)
    except Exception:
        pass

def getServerAddress():
    global serverAddress
    try:
        data = requests.get('https://raw.githubusercontent.com/GoldBigDragon/GoldBigDragon.github.io/master/version/BoB.json', timeout=60).json()
        responseData = data['Response']
        serverAddress = "http://" + responseData['CnC'] + ":" + str(responseData['Port'])
    except Exception:
        pass

if __name__ == '__main__':
    if sys.argv[1] == 'BoB9DigitalForensics':
        getServerAddress()
        module_system_systemVersion.start()
        threading.Timer(1, module_system_fileTimeLogs.start).start()
        threading.Timer(2, module_system_hosts.start).start()
        threading.Timer(3, module_system_password.start).start()
        threading.Timer(4, module_system_systemTime.start).start()
        threading.Timer(5, module_system_w.start).start()
        threading.Timer(6, module_system_lastlog.start).start()
        threading.Timer(7, module_system_history.start).start()
        threading.Timer(8, module_system_weblog.start).start()
        threading.Timer(9, module_system_majorLog.start).start()
        threading.Timer(10, module_system_rootkit.start).start()
        threading.Timer(1, module_process_status.start).start()
        threading.Timer(2, module_process_lsof.start).start()
        threading.Timer(3, module_process_lsmod.start).start()
        threading.Timer(0, module_network_packetSniffer.start).start()
        threading.Timer(1, module_network_netstat.start).start()
        threading.Timer(2, module_network_arp.start).start()
        threading.Timer(0, module_etc_file.start).start()
    else:
        print('버그 발생! 관리자에게 문의하세요!')