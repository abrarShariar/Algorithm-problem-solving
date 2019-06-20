var removeElement = function(nums, val) {
  nums = nums.sort((a,b) => a - b);
  let i = 0;
  let j = i+1;

  while (i < nums.length) {
    if (nums[i] !== val) {
      i++;
      j++;
    } else {
      while (j < nums.length) {
        if (nums[j] !== val) {
          nums[i] = nums[j];
          i++;
        }
        j++;
      }
      break;
    }
  }

  // console.log(nums);
  // console.log(i);
  return i;
};

removeElement([2,0,1,2,3], 2);
removeElement([2,0,1,2,3], 3);
removeElement([2,3,3], 2);
