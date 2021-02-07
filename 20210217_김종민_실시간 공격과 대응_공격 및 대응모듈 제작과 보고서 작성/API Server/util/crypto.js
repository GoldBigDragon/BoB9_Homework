var CryptoJS = require("crypto-js");
var sttobi = require("string-to-binary");
var bitost = require("binary-to-string");
const key = "DaJaBJo_SeRvErApI_gOlD_bIg_DrAgOn";

//aes로 암호화 한 후 base64로 다시 암호화
exports.encrypt = function(text) {
  var ciphertext = CryptoJS.AES.encrypt(text, key);
  var wordArray = CryptoJS.enc.Utf8.parse(ciphertext);
  var wordkey = CryptoJS.enc.Base64.stringify(wordArray);
  var finalkey = sttobi(wordkey);
  return finalkey;
};

//복호화 암호화의 과정을 역순으로
exports.decrypt = function(text) {
  var binarykey = bitost(text);
  var parsedWordArray = CryptoJS.enc.Base64.parse(binarykey.toString());
  var parsedStr = parsedWordArray.toString(CryptoJS.enc.Utf8);
  var bytes = CryptoJS.AES.decrypt(parsedStr, key);
  var plaintext = bytes.toString(CryptoJS.enc.Utf8);
  return plaintext;
};
