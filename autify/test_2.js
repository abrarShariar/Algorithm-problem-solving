'use strict';

const fs = require('fs');
const https = require('https');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
    return inputString[currentLine++];
}


async function getMovieList(year) {
    // write your code here
    // API endpoint: https://jsonmock.hackerrank.com/api/movies?Year=<year>
    https.get(`https://jsonmock.hackerrank.com/api/movies?Year=${year}`, (res) => {
        var body = "";

        res.on("data", (chunk) => {
            body += chunk;
        })

        res.on("end", () => {
            console.log(body);
            let response = JSON.parse(body);

            console.log(response['data']);

            let all_titles = response['data'].map(data => {
                return data['Title'];
            })

            console.log(all_titles);

            return new Promise((resolve, reject) => {
                return resolve(all_titles);
            });
        })
    });
}

async function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const year = readLine().trim();

  const results = await getMovieList(year);
    
  if (results.length > 0) {
      for (const result of results) {
        ws.write(`${result}\n`);
      }
  } else {
       ws.write('No Results Found');
  }

  ws.end();
}