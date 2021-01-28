# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:05:03 2021

@author: GoldBigDragon
"""
"""
alter table Historys add status  VARCHAR(20);
alter table Historys change path filepath  LONGTEXT;
alter table Historys change group user_gruop LONGTEXT;
"""

# 명령어 사용을 위한 라이브러리
import subprocess
# 웹 연결을 위한 라이브러리
import requests
# json 형태로 값을 넘기기 위한 라이브러리
import json
# 날짜 계산을 위한 라이브러리
from datetime import datetime

# 개인 PC 실험용 MySQL 라이브러리. pip install pymysql 명령어 입력이 필요하다.
import pymysql
import threading
import re


# [고칠 필요 없음] 데이터가 수집 될 API 서버 주소
# (테스트 시 db.sql내용대로 DB 구성 후, 본인 주소로 고쳐서 사용하기!)
global serverAddress
serverAddress = 'http://192.168.219.100:3123'

global ORIGINAL_HISTORY
ORIGINAL_HISTORY = []
    
# [고칠 필요 없음] 명령어 실행 후 화면에 뿌려지는 출력 값을 반환하는 함수
def runCommand(command):
    output = subprocess.getoutput(command)
    return output

# [고칠 필요 없음] 현재 시각을 반환하는 함수. 현재 시간을 인자로 넣어야 할 경우 사용하자!
def getNow():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def getHistory():
    History = []
    output = runCommand('bash -i -c "history -r; history | tail -30"')
    lines = output.split('\n')
    for row in lines:
        #print("row : " + row)
        #if ',' not in row and ':' in row:
        History.append(row)
    return History


def runThread():
    print('Running...')
    History =  getHistory()
    if (History != ORIGINAL_HISTORY):
        for history in History:
            if history not in ORIGINAL_HISTORY:
                #sendApiServer(filetime, 'ADD')
                insertMySQL(history, 'ADD')
                ORIGINAL_HISTORY.append(history)

        #removedFiles = list(set(ORIGINAL_FIELTIMELOGS) - set(History))
        #for removed in removedFiles:
        #    #sendApiServer(filetime, 'DEL')
        #    insertMySQL(filetime, 'DEL')
        #    ORIGINAL_FIELTIMELOGS.remove(removed) # delete file log
    threading.Timer(5, runThread).start()

# [수정 필요] API서버로 데이터를 전송하는 함수.
def sendApiServer(History, status):
    global serverAddress
    
    # subUrl은 WBS를 참고한다! API 서버가 열어 둔 통신은 제한적이기 때문!
    subUrl = '/system/post-history'

    # 데이터 타입명은 db.sql 파일을 참고한다! MySQL 컬럼 명과 동일해야하기 때문!
    nowTime = getNow()
    # 첫 줄은 테이블 Title 부분이라 range를 1로 시작하였음!
    # Title도 필요하다면 0으로 변경하거나 지우기!
    tabs = re.sub(' +', ' ', History).split(' ',maxsplit=5)
    historytime = tabs[2] + ' ' + tabs[3]
    data = {'time': historytime, 'command': tabs[5], 'vid': tabs[1]}
    try:
        requests.post(serverAddress + subUrl, data=json.dumps(data), timeout=60)
    except requests.exceptions.Timeout:
        print('Time out')

# [수정 자유] 개인 PC 실험 시 사용하면 되는 함수.
# INSERT문만 확인하면 된다!
def insertMySQL(history, status):
    #print(history)
    conn = pymysql.connect(host='localhost', user='root', password='root', db='realtimeResponse', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO `realtimeResponse`.`History` (time, command, vid) VALUES(%s, %s, %s);"
     
    tabs = re.sub(' +', ' ', history).split(' ',maxsplit=5)
    historytime = tabs[2] + ' ' + tabs[3]
    # 끝에 , 반점 지우지 말것! 항상 끝은 반점으로 끝낼것!
    print(sql,( historytime, tabs[5],tabs[1], ))
    cursor.execute(sql,( historytime, tabs[5],tabs[1], ))
    conn.commit()
    conn.close()

# [수정 필요] python 실행 시 가장 먼저 실행되는 함수
if __name__ == '__main__':
    # 커맨드 수정하기!
    
    ## 이 구문에 주석을 하면 초기 수집 가능 
    #ORIGINAL_HISTORY = getHistory()
    
    runThread()
    #output = runCommand("ls /bin/ --time-style='+%Y-%m-%d %H:%M:%S' -alt 2> /dev/null | grep ^- | head -2")
    #sendApiServer(output)
    # 아래 #을 지우고, 위 sendApiServer 앞에 #을 붙임으로 써 본인 PC에 바로 테스트가 가능해진다!
    #insertMySQL(output)