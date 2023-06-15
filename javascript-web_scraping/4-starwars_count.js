#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let film;
let films;
let character;
let characters;
let number = 0;

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    films = JSON.parse(body).results;
    for (film in films) {
      characters = films[film].characters;
      for (character in characters) {
        if (characters[character].includes('18')) {
          number++;
        }
      }
    }
    console.log(number);
  }
});
