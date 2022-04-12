#!/usr/bin/node
const rs = require('request');
rs(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  error && console.log(error);
  console.log(JSON.parse(body).title);
});
