#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	}
    }

    print () {
	let a = 'X'.repeat(this.width) + '\n';
	a = a.repeat(this.height);
	console.log(a.slice(0, -1));
    }

    rotate () {
	[this.height, this.width] = [this.width, this.height];
    }

    double () {
	[this.height, this.width] = [this.height * 2, this.width * 2];
    }
}
module.exports = Rectangle;
