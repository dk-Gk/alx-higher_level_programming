#!/usr/bin/node
const fs = require('fs');
const rs = require('request');
rs(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
