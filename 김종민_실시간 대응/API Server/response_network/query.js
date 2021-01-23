const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();

module.exports = {
  // GET
  getArp: (param, callback) => {
    const selectQuery = "SELECT * FROM `realtimeResponse`.`arp` WHERE time >= ? AND time <= ?;";
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
  insertArp: (post, callback) => {
    const updateQuery = "INSERT INTO `realtimeResponse`.`arp` (time, address, hardwareType, hardwareAddress, interface) VALUES(?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.address, post.hardwareType, post.hardwareAddress, post.interface], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
};