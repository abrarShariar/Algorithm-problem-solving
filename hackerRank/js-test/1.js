'use strict';

const fs = require('fs');

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
class StaffList {
    constructor () {
        this.staffCollection = {};
    }
    //add your code here
    add (name, age) {
        if (age > 20) {
            this.staffCollection[name] = age;
        } else {
            throw "Error: Staff member age must be greater than 20";
        }
    }

    remove (name) {
        if (name in this.staffCollection) {
            delete this.staffCollection[name];
            return true;
        }

        return false;
    }

    getSize () {
        return Object.keys(this.staffCollection).length;
    }
}
function main() {