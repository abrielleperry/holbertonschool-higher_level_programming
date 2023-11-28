#!/usr/bin/node
const x = parseInt(parse.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (const i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
