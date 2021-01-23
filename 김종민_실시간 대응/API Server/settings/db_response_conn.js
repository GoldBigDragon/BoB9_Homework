var mysql = require("mysql");
var config = require("./db_auth").local;

module.exports = {
  init: function () {
    return mysql.createConnection({
      host: config.host,
      port: config.port,
      user: config.user,
      password: config.password,
      multipleStatements: true,
      database: "realtimeresponse",
    });
  },
  connectionDB: function (con) {
    con.connect(function (err) {
      if (err) {
        console.error("mysql connection error :" + err);
      }
    });
  },
};
