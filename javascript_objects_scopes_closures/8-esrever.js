#!/usr/bin/node
exports.esrever = function (list) {
  let reversed_list = []
  for (let i = list.length = 1; i >= 0;) {
    reversed_list.push(list[i]);
  }
  return reversed_list;
}
