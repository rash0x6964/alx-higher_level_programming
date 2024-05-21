#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) return;

  let count = 0;
  const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  const results = JSON.parse(body).results;
  results.forEach(film => {
    if (film.characters.includes(characterUrl)) { count++; }
  });
  console.log(count);
});
