const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();

module.exports = {
  //POST
  insertLog: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeattack`.`attacklog` (time, type, message) VALUES(?, ?, ?);";
    con.query(updateQuery, [post.time, post.type, post.message], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
};