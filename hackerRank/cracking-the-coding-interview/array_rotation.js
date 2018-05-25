
const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = ''; 
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    console.log("From END");
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the solve function below.
function solve(a, d) {
  for(let i=0;i<d;i++){
    let removed = a.splice(0,1);
    a.push(removed[0]);
  }
  return a;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nd = readLine().split(' ');

    const n = parseInt(nd[0], 10);

    const d = parseInt(nd[1], 10);

    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));
    
    let result = solve(a, d);
    
    ws.write(result.join(" ") + "\n");
    
    ws.end();
}