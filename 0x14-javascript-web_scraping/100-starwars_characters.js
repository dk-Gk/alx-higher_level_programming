#!/usr/bin/node
const rs = require('request');
const STAR_WAR = `http://swapi.co/api/films/${process.argv[2]}`;
rs(STAR_WAR, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  for (const STAR_WAR of JSON.parse(body).characters) {
    rs(STAR_WAR, (error, response, body) =>
      !error && console.log(JSON.parse(body).name));
  }
});
