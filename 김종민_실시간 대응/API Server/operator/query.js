const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();
const fs = require('fs');

module.exports = {
  // GET
  getCommand: (param, callback) => {
    const selectQuery = param.command;
    con.query(selectQuery, (err, rows) => {
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
  getDownloadTargets: (param, callback) => {
    const selectQuery = "SELECT id, filePath, isDir FROM `realtimeResponse`.`filedownload` WHERE complete = 0;";
    con.query(selectQuery, (err, rows) => {
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
  }, getNeedRemoveTarget: (param, callback) => {
    const selectQuery = "SELECT `id`, directoryName, fileName FROM `realtimeattack`.`createfiles`;";
    con.query(selectQuery, (err, rows) => {
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
  }, createDir: (param, callback) => {
    const dirPath = "D:\\엔터테이먼트\\문서\\BoB 9기\\과제\\3차\\김종민_실시간 대응\\API Server\\uploads\\" + param.path.replace('/', "\\");
    const isExists = fs.existsSync( dirPath );
    if( !isExists ) {
        fs.mkdirSync( dirPath, { recursive: true } );
    }
    callback(null, null);
  },
  //POST
  postCommand: (post, callback) => {
    const selectQuery = post.command;
    con.query(selectQuery, (err, rows) => {
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
  addFileDownloadTarget: (post, callback) => {
    const insertQuery = "INSERT IGNORE INTO `realtimeResponse`.`filedownload` (filePath, isDir) VALUES(?, ?);";
    con.query(insertQuery, [post.filePath, post.isDir], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  updateFileDownloadTarget: (post, callback) => {
    const updateQuery = "UPDATE `realtimeResponse`.`filedownload` SET complete = 1 WHERE `id` = ?;";
    con.query(updateQuery, [post.id], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
};