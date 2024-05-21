#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) return;

  const todos = JSON.parse(body);
  const completedTasks = todos.reduce((acc, todo) => {
    if (todo.completed) { acc[todo.userId] = (acc[todo.userId] || 0) + 1; }
    return acc;
  }, {});

  console.log(completedTasks);
});
