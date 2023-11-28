#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arg1 = process.argv.slice(2).map(Number);
  arg1.sort((a, b) => b - a);
  console.log(arg1[1]);
}
