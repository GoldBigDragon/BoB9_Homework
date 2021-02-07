const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();

module.exports = {
  //POST
  insertPacket: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeattack`.`packettraffic` (time, protocol, sourceIp, sourcePort, destIp, destPort, header, data) VALUES(?, ?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.protocol, post.sourceIp, post.sourcePort, post.destIp, post.destPort, post.header, post.data], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
};