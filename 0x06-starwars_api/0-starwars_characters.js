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
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch film: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Fetch and print each character in order
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) return reject(new Error(err)); // Reject with Error object
        if (res.statusCode !== 200) return reject(new Error(`Failed: ${res.statusCode}`)); // Reject with Error object
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  // Handle the asynchronous requests sequentially
  (async () => {
    for (const characterUrl of characterUrls) {
      try {
        const name = await fetchCharacter(characterUrl);
        console.log(name);
      } catch (err) {
        console.error(err.message); // Log the error message
      }
    }
  })();
});
