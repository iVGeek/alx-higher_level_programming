#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
// console.log(
  let array = process.argv.filter(ele => parseInt(ele));
  array = array.filter(ele => ele < Math.max(...array));
  console.log(Math.max(...array));
// )
}
