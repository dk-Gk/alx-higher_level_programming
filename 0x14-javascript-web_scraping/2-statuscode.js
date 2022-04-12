#!/usr/bin/node
const rs = require('request');
rs(process.argv[2], function (error, response, body) {
  error && console.log(error);
  response && console.log('code:', response.statusCode);
});
