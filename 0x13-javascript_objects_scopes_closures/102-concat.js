#!/usr/bin/node
const fs = require('fs');

const Arg1 = fs.readFileSync(process.argv[2], 'utf8').toString();
const Arg2 = fs.readFileSync(process.argv[3], 'utf8').toString();
fs.writeFileSync(process.argv[4], Arg1 + Arg2);
