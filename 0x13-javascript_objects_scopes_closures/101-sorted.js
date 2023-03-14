#!/usr/bin/node

const dic1 = require('./101-data').dict;
const dic2 = {};
for (const key in dic1) {
  if (dic2[dic1[key]] === undefined) {
    dic2[dic1[key]] = [key];
  } else {
    dic2[dic1[key]].push(key);
  }
}
console.log(dic2);
