#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  newDict[value] = newDict[value] || [];
  newDict[value].push(key);
}
console.log(newDict);
