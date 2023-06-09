#!/usr/bin/node
const [arg] = process.argv.slice(2);
const number = parseInt(arg);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
