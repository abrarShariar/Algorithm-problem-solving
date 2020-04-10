const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let counter = 0;
const evenLowest = 2;
rl.on('line', (line) => {
    if (counter) {
        let num = parseInt(line);
        // let sumOG = ((num + 1)/2) * num;
        // let sumEv = 
        console.log(num)
    }
    counter++;
})
