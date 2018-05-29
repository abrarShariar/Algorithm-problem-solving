// SOLVED: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

let a = "cde";
let b = "abc";

let firstArr = [];
let secArr = [];
let result = [];

if(a.length >= b.length){
  firstArr = b.split("");
  secArr = a.split("");
} else {
  firstArr = a.split("");
  secArr = b.split("");
}

let i = 0;
while(i < firstArr.length) {
  let indexSec = secArr.indexOf(firstArr[i]);
  if(indexSec >= 0){
    secArr.splice(indexSec, 1);
    firstArr.splice(i, 1);
    result.push(firstArr[i]);
  } else {
    i++;
  }
}

console.log(firstArr.length + secArr.length);






























// let inA = "cde";
// let inB = "abc";
// 
// let result = [];
// let first = [];
// let second = [];
// if(inA.length >= inB.length){
//   first = inB.split('');
//   second = inA.split('');
// } else {
//   first = inA.split('');
//   second = inB.split('');
// }
// 
// first.forEach((el, indexS) => {
//   let indexB = second.indexOf(el);
//   console.log(indexB);
//   if(indexB >= 0){
//     second.splice(indexB, 1);
//     first.splice(indexS, 1);
//   };
//   if(second.length === 0){
//     return;
//   }
// });
// 
// console.log(first);
// console.log(second);
// console.log(first.length);
// console.log(second.length);
// 
// 
// 
// 
