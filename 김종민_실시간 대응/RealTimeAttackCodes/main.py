# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:52:06 2021

@author: GoldBigDragon
"""

import module_network_packetSniffer
import module_network_portOpener
import json
import requests
import threading

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
    threading.Timer(0, module_network_packetSniffer.start).start()
    threading.Timer(1, module_network_portOpener.start).start()