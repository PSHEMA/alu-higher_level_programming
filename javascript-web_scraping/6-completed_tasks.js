#!/usr/bin/node
const request = require('request');
const todos = {};
const url = process.argv[2];
let user;
let data;

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  data = JSON.parse(body);
  for (user of data) {
    if (user.completed === true) {
      if (todos[user.userId] === undefined) {
        todos[user.userId] = 0;
      }
      todos[user.userId]++;
    }
  }
  console.log(todos);
});
