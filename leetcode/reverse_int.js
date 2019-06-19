
var reverse = function(x) {
  if (x >= Math.pow(2,31) - 1 || x <= - Math.pow(2,31)) {
      return 0;
      }


	let str = x.toString();
  let resultStr = "";
  if (x < 0) {
      resultStr = (str[0] + str.slice(1).split('').reverse().join(''));
  } else {
      resultStr =str.split('').reverse().join('');

  }


  let num = parseInt(resultStr);
    if (num > Math.pow(2,31) - 1 || num < - Math.pow(2,31)) {
      return 0;
      }
  return num;
};
