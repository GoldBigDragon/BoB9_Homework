const sqlConn = require("../settings/db_response_conn");
const con = sqlConn.init();

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
};