#!/usr/bin/node
const args = process.argv;
let b1 = 0;
let b2 = 0;
let num;
if (process.argv.length < 4) {
    console.log('0');
} else {
    for (let i = 2; i < args.length; i++) {
	num = parseInt(args[i]);
	if (num > b1) {
	    b2 = b1;
	    b1 = num;
	} else if (num > b2) {
	    b2 = num;
	}
    }
    console.log(b2);
}
