#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie details using the Star Wars API
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(new Error(`Failed to fetch film: ${error.message}`));
    return;
  }

  if (response.statusCode !== 200) {
    console.error(new Error(`Failed to fetch film: HTTP ${response.statusCode}`));
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Function to fetch a character's name
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          return reject(new Error(`Failed to fetch character: ${err.message}`));
        }
        if (res.statusCode !== 200) {
          return reject(new Error(`Failed to fetch character: HTTP ${res.statusCode}`));
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  // Process characters sequentially
  (async () => {
    for (const characterUrl of characterUrls) {
      try {
        const name = await fetchCharacter(characterUrl);
        console.log(name);
      } catch (err) {
        console.error(err.message);
      }
    }
  })();
});
