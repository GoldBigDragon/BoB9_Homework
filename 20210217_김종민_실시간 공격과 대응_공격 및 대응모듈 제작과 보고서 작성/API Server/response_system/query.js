const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();

module.exports = {
  // GET
  // n초 이상 차이나는 경우 반환
  getTimeDifference: (param, callback) => {
    const selectQuery = "SELECT * FROM `realtimeresponse`.`systemtime` WHERE TIME_TO_SEC(`systemTime`) - TIME_TO_SEC(`time`) > ? OR TIME_TO_SEC(`systemTime`) - TIME_TO_SEC(`time`) < ?;";
    con.query(selectQuery, [param.second, (-1 * param.second)], (err, rows) => {
      if (err) {
        console.log(err);
        callback(err, { result: "fail" });
      } else {
        if (rows.length > 0) {
          callback(err, rows);
        } else {
          callback(err, null);
        }
      }
    });
  },
  //POST
  insertHosts: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`hosts` (time, status, address) VALUES(?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.address], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertHistory: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`history` (num, time, command) VALUES(?, ?, ?);";
    con.query(updateQuery, [post.num, post.time, post.command], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertFileTimeLog: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`filetimelogs` (time, permission, user, userGroup, size, filePath) VALUES(?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.permission, post.user, post.userGroup, post.size, post.filePath], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertSystemTime: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`systemtime` (time, systemTime) VALUES(NOW(), ?);";
    con.query(updateQuery, [post.systemTime], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertSystemVersion: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`systemversion` (time, externalIp, localIp, systemVersion) VALUES(?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.externalIp, post.localIp, post.systemVersion], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertAccountActivity: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`accountactivity` (time, upTime, loginUsers, user, tty, connectFrom, loginTime, what) VALUES(?, ?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.upTime, post.loginUsers, post.user, post.tty, post.connectFrom, post.loginTime, post.what], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertAccountPasswd: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`accountpasswd` (time, status, user, uid, gid, name, homeDir, loginShell) VALUES(?, ?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.user, post.uid, post.gid, post.name, post.homeDir, post.loginShell], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertLastLog: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`lastlog` (time, status, username, data) VALUES(?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.username, post.data], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertWebLog: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`weblogs` (`time`, ip, method, param, `ssl`, `code`, size, `path`, datas) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.ip, post.method, post.param, post.ssl, post.code, post.size, post.path, post.datas], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertMajorLog: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`majorlogs` (time, status, path, user, message) VALUES(?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.path, post.user, post.message], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
};