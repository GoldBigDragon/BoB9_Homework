# 아래 내용은 서버 비밀번호에 맞게 변경하여 실행하기!
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '본인 MySQL 계정 비밀번호';
SET GLOBAL max_allowed_packet=67108864;

CREATE DATABASE IF NOT EXISTS `realtimeResponse`;
USE `realtimeResponse`;

#####시스템#####
# 대상 : 루트킷 탐지 프로그램
# 기록 요지 : 루트킷 탐지 프로그램을 실시간으로 돌릴 수 있을 경우, 변조 파일 탐지를 위함.
CREATE TABLE IF NOT EXISTS `Rootkit` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `path` LONGTEXT DEFAULT NULL,
  `modifiedTime` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ hosts
# 기록 요지 : n초에 1회 수집. HOSTS파일 변조 탐지를 위함
CREATE TABLE IF NOT EXISTS `Hosts` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `address` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ history
# 기록 요지 : n초에 1회 수집. 침투 동향을 파악하기 위함.
CREATE TABLE IF NOT EXISTS `History` (
  `num` INT(11),
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `command` longtext DEFAULT NULL,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ date
# 기록 요지 : n초에 1회 수집. 서버 시간 변조를 탐지하기 위함.
CREATE TABLE IF NOT EXISTS `SystemTime` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` DATETIME,
  `systemTime` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ cat /etc/passwd
# 기록 요지 : n초에 1회 수집. 계정 정보 변경을 탐지하기 위함.
CREATE TABLE IF NOT EXISTS `AccountPasswd` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `user` LONGTEXT,
  `uid` INT(11),
  `gid` INT(11),
  `name` LONGTEXT,
  `homeDir` LONGTEXT,
  `loginShell` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ w
# 기록 요지 : 계정 사용 정보를 n초에 1회 수집. 침투 여부를 알기 위함.
CREATE TABLE IF NOT EXISTS `AccountActivity` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `upTime` VARCHAR(20),
  `loginUsers` INT(11),
  `user` VARCHAR(40),
  `tty` VARCHAR(40),
  `connectFrom` VARCHAR(40),
  `loginTime` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `what` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ cat /proc/version
# 기록 요지 : 시스템 정보를 확인하기 위함.
CREATE TABLE IF NOT EXISTS `SystemVersion` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `systemVersion`LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

#####로그#####
# 대상 : $ lastlog
# 기록 요지 : 로그인 내역을 n초에 1회 수집. 루트 딴 시각을 알기 위함.
CREATE TABLE IF NOT EXISTS `LastLog` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `username` LONGTEXT,
  `data` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : 웹 로그파일
# 기록 요지 : 웹 서버가 '있다면' 기록 되는 웹 로그를 실시간 기입.
CREATE TABLE IF NOT EXISTS `WebLogs` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `method` VARCHAR(10),
  `user` LONGTEXT,
  `message` LONGTEXT,
  `size` INT(11),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : /var/log/auth.log, /var/log/cron, /var/log/secure, /var/log/xferlog, /var/log/message, /var/log/utmp, /var/log/wtmp
# 기록 요지 : 서버에 자동 기입 되는 로그 내용을 실시간 기입.
CREATE TABLE IF NOT EXISTS `Logs` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `path` LONGTEXT,
  `user` LONGTEXT,
  `message` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : 변조 위험이 있는 파일
# 기록 요지 : 감사 대상 파일을 n초에 1회 확인하여 아래 정보를 기입.
CREATE TABLE IF NOT EXISTS `FileTimeLogs` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `permission` VARCHAR(20),
  `user` LONGTEXT,
  `userGroup` LONGTEXT,
  `size` INT(11),
  `filePath` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

#####프로세스#####
# 대상 : $ ps -aux, $ pstree -a, $ lsmod, $ ps -eaf
# 기록 요지 : n초에 1회 수집. 프로세스 수행 내역을 추적하기 위함.
CREATE TABLE IF NOT EXISTS `ProcessStatus` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `uid` LONGTEXT,
  `pid` INT(11),
  `ppid` INT(11),
  `startTime` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `cmd` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ lsmod
# 기록 요지 : n초에 1회 수집. 프로세스 수행 내역을 추적하기 위함.
CREATE TABLE IF NOT EXISTS `ProcessLsmod` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `name` LONGTEXT,
  `size` INT(11),
  `used` INT(11),
  `daemon` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ lsof
# 기록 요지 : n초에 1회 수집. 프로세스 프로세스 수행 내역을 확인하기 위함.
CREATE TABLE IF NOT EXISTS `ProcessLsof` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `command` LONGTEXT,
  `pid` INT(11),
  `path` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

#####네트워크#####
# 대상 : netstat -naop
# 기록 요지 : n초에 1회 수집. 백도어, 리버스 백도어 탐지를 위함.
CREATE TABLE IF NOT EXISTS `InternetConnection` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `proto` VARCHAR(10),
  `localAddress` VARCHAR(40),
  `foreignAddress` VARCHAR(40),
  `state` VARCHAR(40),
  `pid` INT(11),
  `programName` LONGTEXT,
  `timer` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $netstat -naop
# 기록 요지 : n초에 1회 수집. 파일 전송 여부를 탐지하기 위함.
CREATE TABLE IF NOT EXISTS `SocketConnection` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `proto` VARCHAR(10),
  `refCnt` INT(11),
  `type` VARCHAR(20),
  `state` VARCHAR(20),
  `iNode` INT(11),
  `pid` INT(11),
  `programName` LONGTEXT,
  `path` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : 패킷 스니퍼
# 기록 요지 : C&C 서버 주소를 탐지하기 위함.
CREATE TABLE IF NOT EXISTS `PacketTraffic` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `protocol` VARCHAR(10),
  `sourceIp` VARCHAR(40),
  `sourcePort` INT(11),
  `destIp` VARCHAR(40),
  `destPort` INT(11),
  `header` VARCHAR(256),
  `data` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

# 대상 : $ arp
# 기록 요지 : ARP 테이블 변조를 탐지하기 위함.
CREATE TABLE IF NOT EXISTS `Arp` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `status` VARCHAR(3),
  `address` VARCHAR(40),
  `hardwareType` VARCHAR(20),
  `hardwareAddress` VARCHAR(40),
  `interface` VARCHAR(40),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

ALTER DATABASE `realtimeResponse` CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `Rootkit` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `History` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `SystemTime` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `AccountPasswd` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `AccountActivity` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `SystemVersion` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `LastLog` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `WebLogs` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `Logs` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `FileTimeLogs` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `ProcessStatus` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `InternetConnection` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `SocketConnection` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `PacketTraffic` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `Arp` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE DATABASE IF NOT EXISTS `realtimeAttack`;
USE `realtimeAttack`;

# 대상 : 공격 결과
# 기록 요지 : 공격 성공 여부 확인
CREATE TABLE IF NOT EXISTS `AttackLog` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time` VARCHAR(20) NOT NULL DEFAULT '2021-01-01 00:00:00',
  `type` VARCHAR(10),
  `message` LONGTEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='euckr';

ALTER DATABASE `realtimeAttack` CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `AttackLog` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;