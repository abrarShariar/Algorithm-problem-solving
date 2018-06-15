const readline = require('readline');
const read = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

read.on('line', (line) => {
    let Arr = line.split(' ');
    Arr.unshift(-1);
    buildMaxHeap(Arr);
});


const maxHeapify = (arr, index) => {
  let leftChild = 2*index;
  let rightChild = 2*index + 1;

  if(leftChild >= arr.length() || rightChild >= arr.length()){
    return;
  }

};

const buildMaxHeap = (Arr) => {
  let start = (Arr.length() - 1)/2;
  for(let i=start; i>=1; i--){
    maxHeapify(Arr,i);
  }
};
