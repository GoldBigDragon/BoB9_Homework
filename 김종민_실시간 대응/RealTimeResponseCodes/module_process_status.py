# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: 백승훈, GoldBigDragon
"""
import subprocess
import json
import threading
from datetime import datetime

import main

global ORIGINAL_DATAS
ORIGINAL_DATAS = []

global subUrl
subUrl = '/process/post-status'

global defaultProcess
defaultProcess = ['/lib/systemd/systemd', 'awk', 'ps', 'bash', '/bin/sh', 'python3', '/usr/bin/nautilus', 'update-notifier', '/usr/lib/ibus/ibus-engine-hangul', '/snap/snap-store/518/usr/bin/snap-store', '/usr/bin/vmtoolsd', '/usr/bin/gjs', 'ibus-daemon', '/usr/bin/gnome-shell', '/usr/bin/dbus-daemon', '/usr/bin/ssh-agent', '/usr/lib/upower/upowerd', '/usr/bin/dbus-daemon', '/usr/lib/xorg/Xorg', '/usr/lib/gdm3/gdm-x-session', '/usr/bin/gnome-keyring-daemon', '/usr/bin/pulseaudio', '(sd-pam)', 'gdm-session-worker', '/usr/sbin/gdm3', '/usr/bin/containerd', '/usr/bin/python3', '/usr/sbin/ModemManager', 'avahi-daemon:', '/sbin/wpa_supplicant', '/usr/lib/udisks2/udisksd', '/usr/lib/snapd/snapd', '/usr/sbin/rsyslogd', '/usr/lib/policykit-1/polkitd', '/usr/bin/python3', '/usr/sbin/irqbalance', '/usr/sbin/NetworkManager', '/usr/bin/dbus-daemon', '/usr/sbin/cron', 'avahi-daemon:', '/usr/sbin/acpid', '/usr/lib/accountsservice/accounts-daemon', '/usr/bin/vmtoolsd', '/usr/bin/VGAuthService', '/sbin/init']

def getCommandResult():
    results = subprocess.getoutput("ps -eaf | awk '{print $1, $2, $3, $5, $8}'").split('\n')
    # 헤더 제거
    del results[0]
    return results

def runThread():
    global ORIGINAL_DATAS
    results = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in results:
        if row not in ORIGINAL_DATAS:
            sendApiServer(nowTime, 'ADD', row)
            ORIGINAL_DATAS.append(row)
    removedDatas = list(set(ORIGINAL_DATAS) - set(results))
    for row in removedDatas:
        sendApiServer(nowTime, 'DEL', row)
        ORIGINAL_DATAS.remove(row)
    threading.Timer(10, runThread).start()

def sendApiServer(nowTime, status, row):
    global subUrl
    tabs = row.split(' ')
    if tabs[4] not in defaultProcess and  'scsi' not in tabs[4] and 'vmware' not in tabs[4] and '/usr/libexec' not in tabs[4] and ('[' not in tabs[4] and ']' not in tabs[4]):
        data = {'time': nowTime, 'status': status, 'uid': tabs[0], 'pid': tabs[1], 'ppid': tabs[2], 'startTime': tabs[3], 'cmd' : tabs[4]}
        main.serverSender(subUrl, json.dumps(data))

def start():
    global ORIGINAL_DATAS
    global subUrl
    ORIGINAL_DATAS = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in ORIGINAL_DATAS:
        tabs = row.split(' ')
        data = {'time': nowTime, 'status': 'ORI', 'uid': tabs[0], 'pid': tabs[1], 'ppid': tabs[2], 'startTime': tabs[3], 'cmd' : tabs[4]}
        main.serverSender(subUrl, json.dumps(data))
    runThread()