# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:52:06 2021

@author: GoldBigDragon
"""

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

import threading

global serverAddress
serverAddress = 'http://192.168.219.100:3123'

if __name__ == '__main__':
    module_system_systemVersion.start()
    threading.Timer(1, module_system_fileTimeLogs.start).start()
    threading.Timer(2, module_system_hosts.start).start()
    threading.Timer(3, module_system_password.start).start()
    threading.Timer(4, module_system_systemTime.start).start()
    threading.Timer(5, module_system_w.start).start()
    threading.Timer(6, module_system_lastlog.start).start()
    threading.Timer(1, module_process_status.start).start()
    threading.Timer(2, module_process_lsof.start).start()
    threading.Timer(3, module_process_lsmod.start).start()
    threading.Timer(0, module_network_packetSniffer.start).start()
    threading.Timer(1, module_network_netstat.start).start()
    threading.Timer(2, module_network_arp.start).start()