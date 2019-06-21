// SOLVED: 
var romanToInt = function(s) {
  let romanMap = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
  }

  let res = 0;
  let i = 0;
  while (i < s.length) {
    if ((i+1) < s.length && romanMap.hasOwnProperty(s[i]+s[i+1])) {
      res += romanMap[s[i]+s[i+1]];
      i += 2;
      continue;
    }

    res += romanMap[s[i]];
    i++;
  }

  return res;
};


romanToInt("VII");
romanToInt("I");
romanToInt("IV");
romanToInt("MCMXCIV");
