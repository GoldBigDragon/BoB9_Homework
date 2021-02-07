# 3차 교육 과제 목록
***
`완료` `2021년 01월 12일 화요일 까지`  
### 이경문 - 네트워크
  - 주제 : Snort(Suricata) rule 파일을 제작하여 특정 사이트 트래픽을 탐지하여라.
  - 메일 양식 : [bob9][포렌식]suricata-rule[김태룡]
  - test.rules 파일에 20개의 사이트를 탐지하는 룰을 만든다.
  - 이후 fast.log를 확인하면서 20개의 사이트가 제대로 탐지되는지 확인을 해 본다.
  - 가급적이면 평문 통신(HTTP)이 이루어 지는 사이트 뿐만 아니라 TLS 통신(HTTPS)을 하는 사이트에 대한 탐지를 구현해 본다.
  - git에는 rules 파일과 fast.log 파일을 올릴 것.
  - 메일에는 코드 파일을 첨부하지 말고 git 주소만 알려줄 것.
***
`완료` `2021년 01월 14일 목요일 까지`  
### Niko - CloudBreach
  1. Cloud breach관련 5분 발표 준비하기. (일반 BoB생들 앞에서 발표할 예정)
  - 주제 정하고 나면 [주소](https://docs.google.com/spreadsheets/d/12uuadVE2W2zw6yC_XHbr4_JuEfQ3BeNdprTeaKPiCww/edit#gid=0 "AWS 강의 시트")의 K 컬럼에 적어두기  
  2. 슬라이드는 영어로 작성하되 발표는 한국어로 해도 된다.
  3. 5분간 발표할 영문 자료를 2021.01.14. 까지 PDF로 [이 곳](https://drive.google.com/drive/u/1/folders/11qrCCHO5JymcboJUhBbsGvG9prNX-O2I "Google Drive")에 첨부한다.  
  4. 2021.01.14. 5분간 한국어로 발표할 준비를 한다.  
  5. 발표 자료에는 아래 내용이 포함되어야 한다.  
    5.a. 공격 시나리오 설명  
    5.b. 무엇이 잘못되었나?(취약점)  
    5.c. 어떻게 발견되었나?  
    5.d. 무엇을 강탈 당하였나?  
    5.e. 보안팀은 어떻게 대응하였나?  
    5.f. 어떻게 수정하였나?  
***
`완료` `2021년 01월 17일 일요일 까지`
### 유현 - EnScript
  - C드라이브 아래 hosts 파일을 읽고, 콘솔에 라인 별로 출력하기.  
  - nationalAnthem.txt를 읽고 출력하기. (주의 : 문자 집합이 ‘한국어’이므로 ef.SetCodePage(949)를 사용해야함)  
***
`완료` `2021년 01월 21일 목요일 까지`
### 정승기 - Terraform
  - Terraform 설치  
  - Terraform을 사용하여 EC2 서비스 생성  
  - (반드시 EC2 서비스 종료 후 로그아웃 하기)
***
`완료` `2021년 01월 30일 토요일 까지`
### 강대명 - 대규모 웹 서비스 개발
  - 제출 Email : charsyam@naver.com  
  - 메일 양식 : [BOB9] \[트랙명:이름\] #1 ShortUrl 아키텍처  
  - 주제 : ShortURL 서버가 어떤 식으로 구성될 것이며, 각각이 죽었을 때 어떻게 구동될지 자유로이 적어보기  
***
`완료` `2021년 01월 31일 일요일 까지`  
### 유현 - EnScript
- 수업자료에 첨부된 PDF의 File Parse, Hand-on Practice 내용 모두 EnScript로 작성 해 보기.  
- 제출 이메일 : cyberlab.prof@gmail.com  
- 제출 기한 : 2021.01.31. 까지  
- 항목 :  
  - 파일로 부터 MD5, SHA1 계산 후, CSV파일로 추출하기  
  - 선택 된 파일을 Map DATA형태로 받은 후, VirusTotal에서 MD5값을 조회하고, 회신된 json 객체 파일을 파싱하여 보기 좋게 만들기.  
  - 로컬 디바이스의 MBR(C:\\lab\\MBR.dat)을 복사하기. (DeviceClass를 MBR읽는데 쓰고, LocalFileClass로 파일 복사하기)  
  - 장치로 부터 2블록을 복사한 다음, 로컬 파일에 블록 단위로 저장하기. (예 : Block1.dat, Block2.dat)  
  - 비할당 클러스터의 첫 번째 섹터 내용을 출력하기  
***  
`완료` `2021년 02월 04일 목요일 까지`  
### 전상현 - C++ 프로그래밍과 API 사용
  - 메인 NPC와 엑스트라 NPC를 이용하여 퀘스트 제작하기.  
  - 제작 이후 추출된 DLL파일은 [구글 드라이브](https://drive.google.com/drive/folders/1CVIv9SjCdYxQjXRaGozjxEc6OAss376b "BoB9 MMORPG")에 업로드 하기.  
***
`완료` `2021년 02월 09일 화요일 까지`  
### 유현 - SecurityAI
  - [관련 학습 데이터](https://tinyurl.com/fs4elf9t "텍스트 파일")을 사용하여 언어 구분학습 코드 작성하기.  
***
`완료` `2021년 02월 14일 월요일 까지`  
### Niko - CloudBreach
  1. AWS 서비스를 하나 선택한다.  
    (S3, IAM, EC2, Lambda, RDS, ESS, ECS, VPC, API Gateway, Elastic Beanstalk, KMS, EKS)  
  2. 선택한 서비스에 대한 종단 간 공격 시나리오를 구상한다.  
    (infiltration, lateral movement, exfiltration)  
  3. 탐지 방법을 설계하고 적용한다.  
  4. 시나리오대로 공격을 진행한 다음, 조사 보고서를 작성한다.  
  5. 서비스를 안전하게 만드는 방법에 대한 개선 방안을 작성한다.  
  6. SIEM을 통해 데이터를 수집하고, 분석 가이드라인을 만든다.
  
  - 01월 25일 : 시나리오를 구상한다. (공통 수업 때 발표할 것임)  
  - 01월 31일 : 탐지 방법을 설계하고 적용한다.  
  - 02월 07일 : 조사 보고서를 작성한다.  
  - 02월 14일 : 최종 제출일  
    - 사례 조사를 통해 알게 된 내용으로 시나리오를 구상한다. (여러 서비스를 섞어 구상하는 것이 좋다)  
    - AWS 내 많은 서비스를 사용하는 것도 중요하고, 어떤 로그를 어떻게 저장할지도 중요하다.  
    - 선택한 서비스를 많이 사용하고 있는 사례를 먼저 찾아서 해당 서비스의 영향을 받는 건에 대한 침해 사고를 연구 해 나가는 것이 좋다.  
***
`완료` `2021년 02월 14일 일요일 까지`  
시연 영상 및 프로그램 다운로드 : https://tinyurl.com/y2ehysbr
### 최원영 - PE Generator
  - 목표 : PE파일(x64)을 생성하는 프로그램 만들기
  - 제출방법 : fl0ckfl0ck@hotmail.com
  - 이메일 제목 : [BoB9 디포경연] PE Generator_[이름]
  - 제출사항 : 소스코드, 실행파일, 결과물 시연 영상
  - 평가요소 :  
    ① 사용자로부터 입력 값(Entrypoint, ImageBase, Section Alignment, File Alignment)을 받아 실행가능한 PE파일(64bit)을 생성하는 프로그램을 만들어야한다. (60점) (import table등 없어도 됨. section table은 4개로 고정(text, data, rdata, rsrc))  
    ② GUI로 제작할 것(20점)  
    ③ 랜덤 생성기능을 만들어서 사용자가 지정한 개수의 PE파일을 랜덤 한 이름으로 생성할 수 있도록 할 것.(20점) (사용자가 10개 설정하면 랜덤한 이름의 PE파일 10개 만들어지게 하기)  
  - 되도록 Python으로 작성할 것.
  - 32비트 PE파일 만드는 것과 별반 다를 것이 없음
  - Python PE파일 라이브러리 사용하면 더 쉽게 만들 수 있을 것이라 생각 함.
  - 메시지박스 같은 것 띄울 필요 없음. 정상적인 64비트 PE파일만 생성하면 된다.
  - DLL 로딩 안 해도 됨.
  - Github찾아보면 제너레이터도 일부 구현되어있거나 구조도 나와 있음.
***
`대기` `2021년 02월 8일 월요일 까지`  
### Niko - Cloud Breach
  - 본인이 선택한 토픽과 시나리오에 대하여 멘티들에게 한글로 간략히 발표한다.
  - [AWS Insident Response Guide](https://d1.awsstatic.com/whitepapers/aws_security_incident_response.pdf "가이드라인")을 참고하기.  
  - RunBook이나 PlayBook을 만드는 것도 좋으나, 모든걸 설명할 필요는 없다.  
  - 명확하게 각 이벤트별 심플하게 설명하는 것이 좋다.  
  - 나에게 주어진 주제 : Incident Response in the Cloud  
***
`완료` `2021년 02월 17일 수요일 까지`
### 곽경주 - Effective Yara
  - 주어진 샘플들을 모두 탐지할 수 있는 야라룰을 작성합니다.  
  - 룰의 개수가 적고 창의적일수록 높은 점수를 획득합니다.  
  - [악성코드](https://mega.nz/file/opQFCSpT#yIG97HKRNE7FgmG5IXzK5SBP4GP3jpfDLcPIe2OOu2E "비밀번호 : infected")를 다운로드 받고, VMware에서 실행 할 것.  
  - 제출 Email : kjkwak12@gmail.com (연락처 : 010-2814-4679)  
  - ICON 확인하는 방법도 사용 해 볼 것.  
***
`완료` `2021년 02월 17일 수요일 까지`
### 김영철 - 판례 요약 및 판시
  - 수업에 언급되지 않았던 디지털포렌식 관련 ‘확정’ 판례를 찾아 소논문 형식으로 요약하기.
  - 대검찰청의 ‘[형사법의 신동향](https://tinyurl.com/y4pquf4s "형사법의 신동향 통권 제69호 수록 논문")’ 논문집 양식과 작성요령, 규칙을 참고하여 작성한다.  

| 논문 내용 | 채점기준 |
|:---:|:---:|
| 사건 개요 | 형식을 잘 맞추었는지 |
| 각 심급 별 쟁점 | 표현을 얼마나 잘 하였는지 |
| 과거 판례와의 비교점 | 찾아본 판례가 얼마나 의미 있는 판례인지 |
| Abstract, 목차, 표지 제외 10장 이하 | 용어(적절한 법률 용어를 사용하고 있는지) |  

  - 과제 선정 금지 판례  
    ① 영남위원회 사건 [대법원1999.9.3.선고99도2317, 23181) 판결]  
    ② 일심회 사건 [대법원 2007.12.13. 선고2007도7257판결]  
    ③ 법률의견서 사건 [대법원 2012.5.17. 선고 2009도6788 전원합의체 판결]  
    ④ 전교조 시국선언 사건 [대법원 2011.5.26. 자 2009모1190 결정]  
    ⑤ 종근당 사건[대법원 2015.7.16. 자2011모1839 결정(전원합의체)]  
    ⑥ 통진당 부정경선 사건[대법원 2015.10.15. 자2013모1969 결정]  
    ⑦ 동양물류 사건 [대법원 2012.3.29. 선고 2011도10508 결정]  
    ⑧ 상여금 횡령사건[대법원 2014.2.27. 선고 2013도12155 판결]  
    ⑨ 비망록 제출 사건 [대법원 2008.5.15. 선고2008도1097 판결]  
    ⑩ 사찰 편취 사건 [대법원 2008.6.26. 선고2008도1584 판결]  
    ⑪ 오산시장 아파트 인·허가 비리사건 Ⅰ [대법원 2014.8.26. 선고2011도63035 판결]  
    ⑫ 오산시장 아파트 인/허가 비리사건 Ⅱ [대법원 2014.8.26. 선고2011도6035 판결]  
    ⑬ 통진당 내란음모 사건 [대법원 2015.1.22. 선고2014도10978판결]  
    ⑭ 선거운동원 일당 지급 사건 [대법원 2013.6.13. 선고2012도16001 판결]  
    ⑮ 공직선거법 위반 녹음 파일 사건 [대법원 2014.1.16. 선고2013도7101 판결]  
    ⑯ 왕재산 간첩단 사건 [대법원 2013.7.26. 선고2013도2511 판결]  
  - 해도 되지만, 점수는 기대하지 않는 것이 좋을 판례 (1차 수업은 했지만, 위 항목에 없는 것)  
    ① 원세훈 국정원장 화염병 투척 사건 [2018.3.15. 선고 대법원 2014도11449 판결]  
    ② 미신고 선거사무원 일당 지급 사건 [대법원 2013.6.13. 선고2012도16001 판결]  
  - 법은 나라마다 다르기 때문에 해외 판례는 참고만 한다. (책 추천 : 아서 베스트 - 미국 증거법)
  - 해외 판례를 한다면 주법에 의한 판례인지 연방법에 의한 판례인지도 따져야 한다.
  - 과제 하다가 물어볼 것 있으면 수업 시간에 물어보기.
***
`진행 중` `2021년 02월 17일 수요일 까지` 
### 김종민 - 실시간 공격과 대응
  - `완료` `2021년 01월 14일 목요일 까지` 클래스 다이어그램 제작  
  - `완료` `2021년 01월 14일 목요일 까지` WBS 개발명세서 제작  
  - `완료` `2021년 01월 25일 월요일 까지` 대응 과정에 대한 모든 DFD 작성  
  - `완료` `2021년 01월 25일 월요일 까지` 시간 되면 틈틈히 모듈 개발하기  
  - `완료` `2021년 02월 04일 목요일 까지` 시나리오에대한 POC 검증하기 : 다른 것 들  
  - `완료` `2021년 02월 04일 목요일 까지` 대응 - history 모듈, 암호화 통신 구축하기  
  - `완료` `2021년 02월 04일 목요일 까지` 공격 - 네트워크 패킷 수집, 네트워크 패킷 송신, 포트 개방, 자폭, 암호화 통신 구현하기  
  - `완료` `2021년 02월 04일 목요일 까지` 대응 모듈 실행파일 생성 및 정상 구동 테스트하기  
  - `완료` `2021년 02월 04일 목요일 까지` 대응 전략 생각하기  
  - `완료` `2021년 02월 07일 일요일 까지` 공격 전략 생각하기  
  - `완료` `2021년 02월 07일 일요일 까지` 공격 모듈 실행파일 생성 및 정상 구동 테스트하기  
  - 실시간공격/대응 보고서 작성 및 제출하기.  
  - [노션 페이지1](https://www.notion.so/1-a30e849a5b994a9a8a735e2650b2cbb7 "1차") [노션 페이지2](https://www.notion.so/2-7c5eb300817249e782063e28338dc21c "2차")  
***
`진행 중` `2021년 02월 17일 수요일 까지`  
### 김종현 - 분석 보고서 및 의견서 작성
  - `완료` 2018 DEFCON : VAC Analysis Report 본인이 직접 해 보고 보고서 다시 쓰기   
  - CFReDS 분석하기  
  - DFC2020 300번대 문제 1개 풀어오기  
  - DFC2020 400번대 문제 1개 풀어오기  
  - 부다페스트 협약에 대한 의견 작성 해 오기(A4 10매 이내)  
  - 포렌식과 블록체인에 대한 의견 작성 해 오기(A4 10매 이내)  
