#!/usr/bin/node

const Firstsq = require('./5-square');

class Square extends Firstsq {
  charPrint (char) {
    const c = char || 'X';
    let a = c.repeat(this.width) + '\n';
    a = a.repeat(this.height);
    console.log(a.slice(0, -1));
  }
}
module.exports = Square;
