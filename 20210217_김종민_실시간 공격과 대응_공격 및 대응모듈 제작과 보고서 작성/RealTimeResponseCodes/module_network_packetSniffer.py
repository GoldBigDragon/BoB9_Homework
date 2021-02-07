# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:00:30 2021

@author: GoldBigDragon
"""
import textwrap
import socket
import struct
import binascii
import json
from datetime import datetime

import main

# import pymysql

global subUrl
subUrl = '/network/post-packet'

def printPacketsV4(data, rawData):
    version, headerLength, ttl, proto, sourceIp, destIp, data = ipv4Seg(data)
    """
    header = ''
    protocol = ''
    srcPort = 0
    destPort = 0
    """
    
    if proto == 6:
        protocol = 'TCP'
        srcPort, destPort, sequence, acknowledgment, urg, ack, psh, rst, syn, fin = struct.unpack('! H H L L H H H H H H', rawData[:24])
        header = 'Version:{},HeaderLength:{},TTL:{},Sequence:{},Acknowledgement:{},URG:{},ACK:{},PSH:{},RST:{},SYN:{},FIN:{}'.format(version, headerLength, ttl, sequence, acknowledgment, urg, ack, psh, rst, syn, fin)
        if len(data) > 0:
            if srcPort == 80 or destPort == 80:
                try:
                    sendApiServer(protocol, sourceIp, srcPort, destIp, destPort, header, HTTP(data))
                except:
                    pass
            else:
                sendApiServer(protocol, sourceIp, srcPort, destIp, destPort, header, outputLine(data))
    
    """ 렉 방지를 위해 일단은 TCP만 로깅한다. 아래 기능 사용하려면 위의 블록 주석도 해제 할 것.
    elif proto == 1:
        protocol = 'ICMP'
        icmpType, code, checksum, data = icmpSeg(data)
        header = 'Type:{},Code:{},Checksum:{}'.format(icmpType, code, checksum)
    elif proto == 17:
        protocol = 'UDP'
        srcPort, destPort, length, data = udpSeg(data)
        header = 'Version:{},HeaderLength:{},TTL:{},Length:{}'.format(version, headerLength, ttl, length)
    sendApiServer(protocol, sourceIp, srcPort, destIp, destPort, header, None)
    # insertMySQL(protocol, sourceIp, srcPort, destIp, destPort, header, None)
    """

def ethernetFrame(data):
    proto = ""
    IpHeader = struct.unpack("!6s6sH",data[0:14])
    dstMac = binascii.hexlify(IpHeader[0]) 
    srcMac = binascii.hexlify(IpHeader[1]) 
    protoType = IpHeader[2] 
    nextProto = hex(protoType) 
    if (nextProto == '0x800'): 
        proto = 'IPV4'
    elif (nextProto == '0x86dd'): 
        proto = 'IPV6'
    data = data[14:]
    return dstMac, srcMac, proto, data

def ipv4Seg(data):
    version_header_len = data[0]
    version = version_header_len >> 4
    header_len = (version_header_len & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_len, ttl, proto, ipv4(src), ipv4(target), data[header_len:]

def ipv4(addr):
    return '.'.join(map(str, addr))

def icmpSeg(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

def udpSeg(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

def outputLine(string):
    size=80
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size-= 1
            return '\n'.join([line for line in textwrap.wrap(string, size)])

def sendApiServer(protocol, srcIp, srcPort, dstIp, dstPort, header, rawdata):
    global subUrl
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': nowTime, 'protocol': protocol, 'sourceIp': srcIp, 'sourcePort': srcPort, 'destIp': dstIp, 'destPort': dstPort, 'header': header, 'data': rawdata}
    main.serverSender(subUrl, json.dumps(data))
""" MySQL 사용 시 위의 import pymysql 주석도 해제할 것.
def insertMySQL(protocol, srcIp, srcPort, dstIp, dstPort, header, data):
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = pymysql.connect(host='localhost', user='root', password='root', db='realtimeResponse', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO `realtimeResponse`.`PacketTraffic` (time, protocol, sourceIp, sourcePort, destIp, destPort, header, data) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(sql,(nowTime, protocol, srcIp, srcPort, dstIp, dstPort, header, data, ))
    conn.commit()
    conn.close()
"""
def start():
    conn = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernetFrame(raw_data)
        if eth_proto == 'IPV4':
            printPacketsV4(data, raw_data)