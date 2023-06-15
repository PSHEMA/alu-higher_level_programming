#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + resp.statusCode);
  }
});
