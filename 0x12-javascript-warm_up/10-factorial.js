#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) return 1;
  const n = parseInt(number);
  if (n === 0) return 1;
  return n * factorial(n - 1);
}

const args = process.argv;
console.log(factorial(args[2]));
