const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();

module.exports = {
  //GET
  getProcessLsof: (param, callback) => {
    const selectQuery = "SELECT * FROM `realtimeResponse`.`processlsof` WHERE time >= ? AND time <= ?;";
    con.query(selectQuery, [param.startTime, param.endTime], (err, rows) => {
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
  getProcessStatus: (param, callback) => {
    const selectQuery = "SELECT * FROM `realtimeResponse`.`processstatus` WHERE time >= ? AND time <= ?;";
    con.query(selectQuery, [param.startTime, param.endTime], (err, rows) => {
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
  insertLsmod: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`processlsmod` (time, status, name, size, used, daemon) VALUES(?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.name, post.size, post.used, post.daemon], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertLsof: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`processlsof` (time, status, command, pid, path) VALUES(?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.command, post.pid, post.path], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertStatus: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`processstatus` (time, status, uid, pid, ppid, startTime, cmd) VALUES(?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.uid, post.pid, post.ppid, post.startTime, post.cmd], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
};
