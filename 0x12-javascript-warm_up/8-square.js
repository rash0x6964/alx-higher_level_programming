#!/usr/bin/node

const args = process.argv;
if (isNaN(args[2])) console.log('Missing size');
else {
  const n = parseInt(args[2]);
  for (let i = 0; i < n; i++) console.log('X'.repeat(n));
}
