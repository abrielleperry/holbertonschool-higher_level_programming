#!/usr/bin/node
function factorial (i) {
  if (isNaN(i) || i === 0) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}
const int = parseInt(process.argv[2]);
console.log(factorial(int));
