# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 01:09:29 2021

@author: GoldBigDragon
"""
import random

global characterArray
global nameArray
global dirNameArray
global extensionArray
global dirArray
global commandArray
characterArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
nameArray = ['AttackModule', 'main', 'DaYeon', 'TaeRyong', 'SeoYeon', 'SeongHoon',
                      'HeeJae', 'JongMin', 'JongHyeon', 'YuHyeon', 'MoonBum', 'DoHoon', 'ChangYeob',
                      'GeunYeong', 'HyunSeok', 'da-yeon', 'tae-ryong', 'seo-yeon', 'seong-hoon',
                      'hee-jae', 'jong-min', 'jong-hyeon', 'yu-heyon', 'moon-bum', 'do-hoon',
                      'chang-yeob', 'geun-yeong', 'hyun-seok', 'module', 'attack', 'mellong', '.gitignore',
                      'cpuhp', 'idle_inject', 'migration', 'ksoftirqd', 'rcu_', 'scsi_', '[kthreadd]',
                      '[mm_percpu_wq]', 'kworker', 'kdevtmpfs', 'kauditd', 'khungtaskd', 'oom_reaper',
                      'CMD', '[kthreadd]', '[ksoftirqd-0]', '[kworker0:0H]', '[rcu_sched]', '[rcu_bh]',
                      '[migration-0]', '[watchdog-0]', '[kdevtmpfs]', '[netns]', '[perf]', '[khungtaskd]',
                      '[writeback]', '[ksmd]', '[khugepaged]', '[crypto]', '[kintegrityd]', '[bioset]',
                      '[kblockd]', '[ata_sff]', '[kpsmoused]', '[scsi_eh_2]', '[scsi_tmf_2]', '[scsi_tmf_5]',
                      '[scsi_eh_16]', '[scsi_tmf_24]', '[scsi_tmf_31]', '[bioset]', '[kworker-u257:2]'
                      ]

dirNameArray = ['temp', 'tmp', 'test', 'rootkit', 'hack', 'hacking', 'crack', 'backdoor',
                'log', 'secure', 'security']
extensionArray = ['sh', 'exe', 'txt', 'py', 'pl', 'log', 'c', 'cpp', 'java', 'class', 'css',
                  'php', 'html', 'jsp', 'js', 'rar', 'tar', 'gz', 'tar.gz']
dirArray = ['/', '~/', '../', '/bin', '/dev', 'etc',
            '/etc', '/home', '/lib', '/lib64', '/lost+found',
            '/media', '/mnt', '/opt', '/proc', '/run',
            '/sbin', '/snap', '/srv', '/tmp', '/usr',
            '/var', '/home/user', '/lib/systemd', '/lib/ufw',
            '/lib/xtables', '/lib/modprobe.d', '/lib/open-iscsi',
            '/lib/resolvconf', '/lib/init', '/lib/lsb', '/lib/hdparm',
            '/lib/firmware', '/lib/apparmor','/var/backups', '/var/cache',
            '/var/lib', '/var/local', '/var/log', '/var/mail',
            '/var/opt', '/var/snap', '/var/spool', '/var/www',
            '/var/cache/man', '/var/cache/snapd', '/var/log/fsck',
            '/var/log/installer', '/var/log/mysql', '/var/log/dist-upgrade',
            '/var/www/html', '/var/www/html/static', '/var/www/html/board_file']
commandArray = ['su', 'sudo', 'history', 'history -c', 'ls', 'll', 'ls -a', 'ls -l',
                'ps', 'ps -aux', 'kill', 'lsmod', 'lsof', 'pstree', 'lastlog', 'pwd',
                'whoami', 'sudo useradd hacker', 'sudo useradd usar', 'sudo useradd root',
                'sudo useradd crack', 'sudo useradd intruder']
pythonScriptArray = [["20초 대기", "import time\nif __name__ == '__main__':\n    time.sleep(20)"],
                     ["구구단", "import time\nif __name__ == '__main__':\n    for i in range(9):\n        for i2 in range(9):\n            print(str(i) + ' x ' + str(i2) + ' = ' + str(i*i2))\n            time.sleep(1)"],
                     ["lsof", "import time\nimport subprocess\nif __name__ == '__main__':\n    subprocess.getoutput('lsof')\n    time.sleep(1)"]]

def getRandomExtension():
    global extensionArray
    return extensionArray[random.randint(0, len(extensionArray)-1)]

def getRandomDirectory():
    global dirArray
    return dirArray[random.randint(0, len(dirArray)-1)]

def getRandomCommand():
    global commandArray
    return commandArray[random.randint(0, len(commandArray)-1)]

def getRandomPythonScript():
    global pythonScriptArray
    return pythonScriptArray[random.randint(0, len(pythonScriptArray)-1)]

def getRandomChar(length):
    global characterArray
    returnString = ''
    for i in range(length):
        returnString += characterArray[random.randint(0, 15)]
    return returnString

def getRandomName(extension):
    global nameArray
    randomNumber = random.randint(0, 3)
    if randomNumber == 0:
        return getRandomChar(random.randint(1, 32)) + '.' + extension
    else:
        return nameArray[random.randint(0, len(nameArray)-1)] + '.' + extension

def getRandomDirectoryName():
    global dirNameArray
    randomNumber = random.randint(0, 3)
    if randomNumber == 0:
        return getRandomChar(random.randint(1, 255))
    else:
        return dirNameArray[random.randint(0, len(dirNameArray)-1)]

def getRandomHex():
    global characterArray
    length = random.randint(1, 255)
    returnString = ''
    for i in range(length):
        returnString += '0x' + characterArray[random.randint(0, len(characterArray)-1)] + characterArray[random.randint(0, len(characterArray)-1)]
    return returnString