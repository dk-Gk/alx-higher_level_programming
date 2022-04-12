#!/usr/bin/node
const rs = require('request');
const Star_war = `http://swapi.co/api/films/${process.argv[2]}`;
rs(Star_war, function (error, response, body) {
    if (error) {
	throw new Error(error);
    }
    for (const url of JSON.parse(body).characters) {
	rs(url, (error, response, body) =>
		!error && console.log(JSON.parse(body).name));
    }
});
