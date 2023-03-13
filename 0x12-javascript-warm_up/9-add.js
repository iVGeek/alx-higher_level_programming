#!/usr/bin/node

if (parseInt(process.argv[2])) {
  if (parseInt(process.argv[3])) {
    console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
