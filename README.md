# 과제 목록
***
`완료` `2021년 01월 12일 화요일 까지`  
### snort(suricata) rule 파일을 제작하여 특정 사이트 트래픽을 탐지하기 - 이경문
  - 주제 : Snort(Suricata) rule 파일을 제작하여 특정 사이트 트래픽을 탐지하여라.
  - 메일 양식 : [bob9][포렌식]suricata-rule[김태룡]
  - test.rules 파일에 20개의 사이트를 탐지하는 룰을 만든다.
  - 이후 fast.log를 확인하면서 20개의 사이트가 제대로 탐지되는지 확인을 해 본다.
  - 가급적이면 평문 통신(HTTP)이 이루어 지는 사이트 뿐만 아니라 TLS 통신(HTTPS)을 하는 사이트에 대한 탐지를 구현해 본다.
  - git에는 rules 파일과 fast.log 파일을 올릴 것.
  - 메일에는 코드 파일을 첨부하지 말고 git 주소만 알려줄 것.
***
`2021년 01월 14일 목요일 까지`  
### Cloud Breach 발표 준비 - Niko, 정승기
  - 주제 : cloud breach관련 5분 발표 준비하기. (일반 BoB생들 앞에서 발표할 예정)
  - 슬라이드는 영어로 작성하되 발표는 한국어로 해도 된다.
  - 주제 정하고 나면 [주소](https://docs.google.com/spreadsheets/d/12uuadVE2W2zw6yC_XHbr4_JuEfQ3BeNdprTeaKPiCww/edit#gid=0 "AWS 강의 시트")의 K 컬럼에 적어두기
***
`2021년 02월 14일 일요일 까지`  
### PE Generator 만들기 - 최원영
  - 목표 : PE파일(x64)을 생성하는 프로그램 만들기
  - 제출방법 : fl0ckfl0ck@hotmail.com
  - 이메일 제목 : [BoB9 디포경연] PE Generator_[이름]
  - 제출사항 : 소스코드, 실행파일, 결과물 시연 영상
  - 평가요소 :
    ① 사용자로부터 입력 값(Entrypoint, ImageBase, Section Alignment, File Alignment)을 받아 실행가능한 PE파일(64bit)을 생성하는 프로그램을 만들어야한다. (60점)  
      (import table등 없어도 됨. section table은 4개로 고정(text, data, rdata, rsrc))  
    ② GUI로 제작할 것(20점)  
    ③ 랜덤 생성기능을 만들어서 사용자가 지정한 개수의 PE파일을 랜덤 한 이름으로 생성할 수 있도록 할 것.(20점) (사용자가 10개 설정하면 랜덤한 이름의 PE파일 10개 만들어지게 하기)  
  - 되도록 Python으로 작성할 것.
  - 32비트 PE파일 만드는 것과 별반 다를 것이 없음
  - Python PE파일 라이브러리 사용하면 더 쉽게 만들 수 있을 것이라 생각 함.
  - 메시지박스 같은 것 띄울 필요 없음. 정상적인 64비트 PE파일만 생성하면 된다.
  - DLL 로딩 안 해도 됨.
  - Github찾아보면 제너레이터도 일부 구현되어있거나 구조도 나와 있음.
***
`2021년 02월 17일 수요일 까지`
### 디지털포렌식 관련 확정판례 소논문 요약 - 김영철
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
    ⑪ 오 산시장 아파트 인·허가 비리사건 Ⅰ [대법원 2014.8.26. 선고2011도63035 판결]  
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
