#!/usr/bin/node
const arg1 = process.argv[2];
const int = Number(arg1);

if (isNaN(int)) {
  console.log('Not a number');
} else {
  console.log('My number:' + int);
}
