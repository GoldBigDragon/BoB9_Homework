const http = require("http");
const url = require("url");
const iconv = require("iconv-lite");

const server = http.createServer().listen(3123);

const EventEmitter = require("events");
const getEventHandler = new EventEmitter();
const postEventHandler = new EventEmitter();

const networkQ = require("./response_network/query.js");

// GET
getEventHandler.on("/network/get-arp", networkQ.getArp);

//POST
postEventHandler.on("/network/post-arp", networkQ.insertArp);

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
  const ip = getClientAddress(req);

  let body = "";

  req.on("data", (data) => {
    body += data;
  });

  req.on("end", () => {
    if (req.method === "GET") {
      param.clientIp = ip;
      console.log(`[GET] : (${ip}) ${decoded}\r\n`);
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
      post.clientIp = ip;
      //console.log(`[POST] : (${ip}) ${decoded}`);
      //console.log(`[POST] : (${ip}) ${decoded} [${body}]\r\n`);
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