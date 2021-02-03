# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:52:06 2021

@author: GoldBigDragon
"""

import requests

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

import threading

import json

global serverAddress
serverAddress = 'http://192.168.219.100:3123'

def serverSender(subUrl, data):
    global serverAddress
    # binary
    hexData = {'data':  "b"+"".join("{:02x}".format(ord(c)) for c in data[::-1])}
    try:
        requests.post(serverAddress + subUrl, data=json.dumps(hexData), timeout=60)
    except Exception:
        pass

def getHex(values):
    return

if __name__ == '__main__':
    module_system_systemVersion.start()
    threading.Timer(1, module_system_fileTimeLogs.start).start()
    threading.Timer(2, module_system_hosts.start).start()
    threading.Timer(3, module_system_password.start).start()
    threading.Timer(4, module_system_systemTime.start).start()
    threading.Timer(5, module_system_w.start).start()
    threading.Timer(6, module_system_lastlog.start).start()
    threading.Timer(7, module_system_history.start).start()
    # 수정 이후 활성화 시키기
    # threading.Timer(8, module_system_weblog.start).start()
    threading.Timer(9, module_system_majorLog.start).start()
    threading.Timer(1, module_process_status.start).start()
    threading.Timer(2, module_process_lsof.start).start()
    threading.Timer(3, module_process_lsmod.start).start()
    threading.Timer(0, module_network_packetSniffer.start).start()
    threading.Timer(1, module_network_netstat.start).start()
    threading.Timer(2, module_network_arp.start).start()
