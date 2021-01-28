# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:51:40 2021

@author: GoldBigDragon
"""
import subprocess
import requests
import json
import threading
from datetime import datetime

import main

global ORIGINAL_DATAS
ORIGINAL_DATAS = []

global subUrl
subUrl = '/process/post-lsof'

global defaultProcess
defaultProcess = ['awk', 'lsof', 'sh', 'nautilus', 'gnome-ter', 'cups-brow', 'cupsd', 'fwupd', 'update-no', 'gvfsd-met', 'ibus-engi', 'xdg-docum', 'snap-stor', 'colord', 'dconf-ser', 'gsd-disk-', 'gsd-xsett', 'gsd-wwan', 'gsd-wacom', 'gsd-usb-p', 'gsd-sound', 'gsd-smart', 'gsd-shari', 'gsd-scree', 'gsd-rfkil', 'gsd-print', 'gsd-power', 'gsd-media', 'gsd-keybo', 'gsd-house', 'gsd-datet', 'gsd-color', 'gsd-a11y-', 'gvfsd-tra', 'gjs', 'evolution', 'xdg-permi', 'at-spi2-r', 'ibus-port', 'ibus-x11', 'ibus-exte', 'ibus-memc', 'ibus-daem', 'gnome-she', 'at-spi-bu', 'ssh-agent', 'gnome-ses', 'upowerd', 'gvfs-gpho', 'gvfs-afc-', 'gvfs-mtp-', 'gvfs-goa-', 'gvfs-udis', 'gvfsd-fus', 'gvfsd', 'rtkit-dae', 'Xorg', 'gdm-x-ses', 'gnome-key', 'tracker-m', 'pulseaudi', '(sd-pam)', 'kerneloop', 'whoopsie', 'gdm-sessi', 'gdm3', 'container', 'unattende', 'ModemMana', 'wpa_suppl', 'udisksd', 'systemd-l', 'switchero', 'snapd', 'rsyslogd', 'polkitd', 'networkd-', 'irqbalanc', 'NetworkMa', 'dbus-daem', 'cron', 'avahi-dae', 'acpid', 'accounts-', 'vmtoolsd', 'VGAuthSer', 'systemd-t', 'systemd-r', 'cryptd', 'vmware-vm', 'loop9', 'loop8', 'systemd-u', 'loop7', 'loop6', 'loop5', 'loop4', 'loop3', 'loop2', 'loop1', 'loop0', 'ttm_swap', 'irq/16-vm', 'systemd-j', 'ext4-rsv-', 'jbd2/sda5', 'scsi_eh_9', 'scsi_eh_8', 'scsi_eh_7', 'scsi_eh_6', 'scsi_eh_5', 'scsi_eh_4', 'scsi_eh_3', 'scsi_eh_2', 'mpt/0', 'mpt_poll_', 'charger_m', 'kworker/u', 'zswap-shr', 'kstrp', 'ipv6_addr', 'vfio-irqf', 'scsi_eh_1', 'scsi_tmf_', 'scsi_eh_0', 'acpi_ther', 'irq/55-pc', 'irq/54-pc', 'irq/53-pc', 'irq/52-pc', 'irq/51-pc', 'irq/50-pc', 'irq/49-pc', 'irq/48-pc', 'irq/47-pc', 'irq/46-pc', 'irq/45-pc', 'irq/44-pc', 'irq/43-pc', 'irq/42-pc', 'irq/41-pc', 'irq/40-pc', 'irq/39-pc', 'irq/38-pc', 'irq/37-pc', 'irq/36-pc', 'irq/35-pc', 'irq/34-pc', 'irq/33-pc', 'irq/32-pc', 'irq/31-pc', 'irq/30-pc', 'irq/29-pc', 'irq/28-pc', 'irq/27-pc', 'irq/26-pc', 'irq/25-pc', 'irq/24-pc', 'kthrotld', 'ecryptfs-', 'kswapd0', 'pm_wq', 'watchdogd', 'devfreq_w', 'edac-poll', 'md', 'ata_sff', 'tpm_dev_w', 'blkcg_pun', 'kblockd', 'kintegrit', 'khugepage', 'ksmd', 'kcompactd', 'writeback', 'oom_reape', 'khungtask', 'kauditd', 'rcu_tasks', 'netns', 'kdevtmpfs', 'kworker/1', 'cpuhp/1', 'cpuhp/0', 'idle_inje', 'migration', 'rcu_sched', 'ksoftirqd', 'mm_percpu', 'kworker/0', 'rcu_par_g', 'rcu_gp', 'kthreadd', 'systemd', 'goa-ident', 'goa-daemo']

def getCommandResult():
    results = subprocess.getoutput("lsof | awk '{print $1,$2,$3,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14}'").split('\n')
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

def sendApiServer(time, status, row):
    global subUrl
    global defaultProcess
    tabs = row.split(' ')
    if(tabs[0] in defaultProcess or '/usr/lib/x86_64-linux-gnu/' in tabs[-1] or '/usr/lib/evolution-data-server/' in tabs[-1] or '/usr/libexec/ibus' in tabs[-1] or '/usr/share/' in tabs[-1] or '/var/cache/fontconfig/' in tabs[-1]):
        return
    for i in range(len(tabs)):
        if tabs[-1] == ' ' or tabs[-1] == '':
            del tabs[-1]
        else:
             break
    try:
        data = {'time': time, 'status': status, 'command': tabs[0], 'pid': int(tabs[1]), 'path': tabs[-1]}
        requests.post(main.serverAddress + subUrl, data=json.dumps(data), timeout=60)
    except Exception:
        pass

def start():
    global ORIGINAL_DATAS
    ORIGINAL_DATAS = getCommandResult()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in ORIGINAL_DATAS:
        sendApiServer(nowTime, 'ORI', row)
    runThread()