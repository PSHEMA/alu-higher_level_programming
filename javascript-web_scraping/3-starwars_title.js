#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let info;
request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    info = JSON.parse(body);
    console.log(info.title);
  }
});
