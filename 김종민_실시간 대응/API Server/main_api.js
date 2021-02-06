const http = require("http");
const url = require("url");
const iconv = require("iconv-lite");
const fs = require("fs");
const formidable = require('formidable');

const server = http.createServer().listen(3123);

const EventEmitter = require("events");
const getEventHandler = new EventEmitter();
const postEventHandler = new EventEmitter();

const networkQ = require("./response_network/query.js");
const processQ = require("./response_process/query.js");
const systemQ = require("./response_system/query.js");
const operatorQ = require("./operator/query.js");

const attackNetworkQ = require("./attack_network/query.js");
const attackLogQ = require("./attack_log/query.js");

// GET
getEventHandler.on("/op/get", operatorQ.getCommand);
getEventHandler.on("/file/getTarget", operatorQ.getDownloadTargets);
getEventHandler.on("/file/getNeedRemoves", operatorQ.getNeedRemoveTarget);
getEventHandler.on("/dir/create", operatorQ.createDir);
getEventHandler.on("/network/get-arp", networkQ.getArp);
getEventHandler.on("/network/get-internet", networkQ.getInternetConnection);
getEventHandler.on("/network/get-socket", networkQ.getSocketConnection);
getEventHandler.on("/process/get-lsof", processQ.getProcessLsof);
getEventHandler.on("/process/get-status", processQ.getProcessStatus);

//POST
postEventHandler.on("/op/post", operatorQ.postCommand);
postEventHandler.on("/file/addTarget", operatorQ.addFileDownloadTarget);
postEventHandler.on("/file/updateTarget", operatorQ.updateFileDownloadTarget);
postEventHandler.on("/network/post-arp", networkQ.insertArp);
postEventHandler.on("/network/post-conn", networkQ.insertInternetConnection);
postEventHandler.on("/network/post-socks", networkQ.insertSocketConnection);
postEventHandler.on("/network/post-packet", networkQ.insertPacket);
postEventHandler.on("/process/post-lsmod", processQ.insertLsmod);
postEventHandler.on("/process/post-lsof", processQ.insertLsof);
postEventHandler.on("/process/post-status", processQ.insertStatus);
postEventHandler.on("/system/post-hosts", systemQ.insertHosts);
postEventHandler.on("/system/post-history", systemQ.insertHistory);
postEventHandler.on("/system/post-file", systemQ.insertFileTimeLog);
postEventHandler.on("/system/post-time", systemQ.insertSystemTime);
postEventHandler.on("/system/post-info", systemQ.insertSystemVersion);
postEventHandler.on("/system/post-w", systemQ.insertAccountActivity);
postEventHandler.on("/system/post-passwd", systemQ.insertAccountPasswd);
postEventHandler.on("/system/post-lastlog", systemQ.insertLastLog);
postEventHandler.on("/system/post-web", systemQ.insertWebLog);
postEventHandler.on("/system/post-major", systemQ.insertMajorLog);

postEventHandler.on("/attack/network/post-packet", attackNetworkQ.insertPacket);
postEventHandler.on("/attack/post-log", attackLogQ.insertLog);
postEventHandler.on("/attack/post-createFile", attackLogQ.insertFileCreateLog);
postEventHandler.on("/attack/post-deleteFile", attackLogQ.updateFileDeleteLog);

server.on("request", (req, res) => {
  if (req.url === "/health") {
    healthCheck(req, res);
  } else if (req.url === "/fileupload") {
      var form = new formidable.IncomingForm();
      form.uploadDir = "D:\\";
      form.parse(req, function (err, fields, files) {
        if (files.filetoupload != null) {
          var oldpath = files.filetoupload.path;
          var newpath = __dirname +'\\uploads\\' + files.filetoupload.name;
          fs.rename(oldpath, newpath, function (err) {
            if (err) throw err;
            res.write('File uploaded and moved!');
            res.end();
          });
        } else {
          res.write('File not uploaded!');
          res.end();
        }
      });
  } else if (req.url==="/fff") {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<html><head><meta charset="utf-8"></head><body><form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form></body></html>');
    return res.end();
  } else {
    commonRequest(req, res);
  }
});

function healthCheck(req, res) {
  res.writeHead(200, {
    "Content-Type": "text/plain",
  });
  res.end("true");
}

function commonRequest(req, res) {
  const strContents = new Buffer.from(req.url, "binary");
  const decoded = iconv.decode(strContents, "UTF-8").toString();
  const Url = url.parse(decoded, true);
  const pathname = Url.pathname;
  const param = Url.query;

  let body = "";

  req.on("data", (data) => {
    body += data;
  });

  req.on("end", () => {
    if (req.method === "GET") {
    //console.log(`[GET] : ${decoded}\r\n`);
      getEventHandler.emit(pathname, param, (err, rows) => {
        if (err) {
          res.writeHead(500, {
            "Content-Type": "text/plain; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
          });
          res.end();
        } else {
          res.writeHead(200, {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
          });
          res.end(JSON.stringify(rows));
        }
      });
    } else if (req.method === "POST") {
      const convert = (from, to) => str => Buffer.from(str, from).toString(to);
      const hexToUtf8 = convert('hex', 'utf8');
      const post = JSON.parse(body);
      realData = JSON.parse(reverseString(hexToUtf8(post.data.substring(1))))
      // console.log(`[POST] : ${realData}`);
      postEventHandler.emit(pathname, realData, (err, rows) => {
        if (err) {
          res.writeHead(500, {
            "Content-Type": "text/plain; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
          });
          res.end();
        } else {
          res.writeHead(200, {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
          });
          res.end(JSON.stringify(rows));
        }
      });
    }
  });
}
function reverseString(str) {
  return str.split("").reverse().join("");
}