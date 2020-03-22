var removeDuplicates = function(nums) {
  let i = 0;
  let j = i+1;

  let countDup = 0;
  while (j < nums.length) {
    if (nums[i] === nums[j]) {
      countDup++;
      if (countDup === 2) {
        let m = i;
        let n = j;
        countDup = 0;
        while (n < nums.length) {
          nums[m] = nums[n];
          m++;
          n++
        }
      } else {
        i++;
        j++;
      }
    } else {
      countDup = 0;
      i++;
      j++;
    }
  }


  console.log(nums);
  console.log(i);

};

removeDuplicates([0,0,1,1,1,1,2,3,3]);
