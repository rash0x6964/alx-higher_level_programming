#!/usr/bin/node

let argCount = 0;
exports.logMe = function (item) {
  argCount++;
  console.log(`${argCount - 1}: ${item}`);
};
