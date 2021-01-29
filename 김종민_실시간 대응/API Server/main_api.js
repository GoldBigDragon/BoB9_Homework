const http = require("http");
const url = require("url");
const iconv = require("iconv-lite");

const server = http.createServer().listen(3123);

const EventEmitter = require("events");
const getEventHandler = new EventEmitter();
const postEventHandler = new EventEmitter();

const networkQ = require("./response_network/query.js");
const processQ = require("./response_process/query.js");
const systemQ = require("./response_system/query.js");
const operatorQ = require("./operator/query.js");

// GET
getEventHandler.on("/op/get", operatorQ.getCommand);
getEventHandler.on("/network/get-arp", networkQ.getArp);
getEventHandler.on("/network/get-internet", networkQ.getInternetConnection);
getEventHandler.on("/network/get-socket", networkQ.getSocketConnection);
getEventHandler.on("/process/get-lsof", processQ.getProcessLsof);
getEventHandler.on("/process/get-status", processQ.getProcessStatus);

//POST
postEventHandler.on("/op/post", operatorQ.postCommand);
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

server.on("request", (req, res) => {
  if (req.url === "/health") {
    healthCheck(req, res);
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
      console.log(`[GET] : ${decoded}\r\n`);
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
      const post = JSON.parse(body);
      //console.log(`[POST] : ${decoded}`);
      //console.log(`[POST] : ${decoded} [${body}]\r\n`);
      postEventHandler.emit(pathname, post, (err, rows) => {
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

function getClientAddress(req) {
  return (
    (req.headers["x-forwarded-for"] || "").split(",")[0] ||
    req.connection.remoteAddress
  );
}