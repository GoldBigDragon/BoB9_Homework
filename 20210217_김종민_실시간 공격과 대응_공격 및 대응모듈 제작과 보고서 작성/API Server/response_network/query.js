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
  getInternetConnection: (param, callback) => {
    const selectQuery = "SELECT * FROM `realtimeResponse`.`internetconnection` WHERE time >= ? AND time <= ?;";
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
  getSocketConnection: (param, callback) => {
    const selectQuery = "SELECT * FROM `realtimeResponse`.`socketconnection` WHERE time >= ? AND time <= ?;";
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
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`arp` (time, status, address, hardwareType, hardwareAddress, interface) VALUES(?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.address, post.hardwareType, post.hardwareAddress, post.interface], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertSocketConnection: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`SocketConnection` (time, status, proto, refCnt, type, state, iNode, pid, programName, path) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.proto, post.refCnt, post.type, post.state, post.iNode, post.pid, post.programName, post.path], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertInternetConnection: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`InternetConnection` (time, status, proto, localAddress, foreignAddress, state, pid, programName, timer) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);";
    con.query(updateQuery, [post.time, post.status, post.proto, post.localAddress, post.foreignAddress, post.state, post.pid, post.programName, post.timer], (err) => {
      if (err) {
        console.log(err);
        callback(err, "fail");
      } else {
        callback(err, "success");
      }
    });
  },
  insertPacket: (post, callback) => {
    const updateQuery = "INSERT IGNORE INTO `realtimeResponse`.`PacketTraffic` (time, protocol, sourceIp, sourcePort, destIp, destPort, header, data) VALUES(?, ?, ?, ?, ?, ?, ?, ?);";
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