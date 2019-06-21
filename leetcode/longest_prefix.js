var longestCommonPrefix = function(strs) {
  let resultStr = strs[0];
  for (let i = 1;i < strs.length;i++) {
    let endIndex = strs[i].length;
    for (let j = 0;j < strs[i].length;j++) {
      if (strs[i][j] !== resultStr[j]) {
        endIndex = j;
        break;
      }
    }
    resultStr = resultStr.slice(0, endIndex);
  }

  return resultStr;
};

longestCommonPrefix(["fl", "flo", "flower", "fuck"])
longestCommonPrefix(["a", "b", "c", "d"])
longestCommonPrefix(["asd"])
