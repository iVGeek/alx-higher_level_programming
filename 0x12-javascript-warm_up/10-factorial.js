#!/usr/bin/node

function fact (nb) {
  if (nb === 1) {
    return (1);
  } else {
    return (nb * fact(nb - 1));
  }
}

if (parseInt(process.argv[2])) {
  console.log(fact(parseInt(process.argv[2])));
} else {
  if (process.argv[2] === undefined) {
    console.log(1);
  } else {
    console.log('NaN');
  }
}
