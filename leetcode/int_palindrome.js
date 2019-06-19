var isPalindrome = function(x) {
  if (x < 0 || x % 10 === 0 && x !== 0) {
    return false;
  }

  let rev = 0;
  while (rev < x) {
    rev = (rev * 10) + (x % 10);
    x = x / 10;
  }

  return x === rev || x === (rev / 10);
};














// var isPalindrome = function(x) {
//
//     if (x < 0 || (x%10 === 0 && x !== 0)) {
//         return false;
//         }
//     else if (x === 0) {
//         return true;
//         }
//   let rev = 0;
//   while (rev < x) {
//     let rem = x % 10;
//     rev = (rev * 10) + rem;
//
//     if (rev === x) {
//       return true;
//     }
//     else if (rev > x) {
//       return false;
//     }
//
//    x = x / 10;
//
//   }
// };
