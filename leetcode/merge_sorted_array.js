// FIX
var merge = function(nums1, m, nums2, n) {
  let i = 0;
  let j = 0;
  while (j < n) {
    if (nums1[m] === 0) {
      if (nums1[i] <= nums2[j]) {
        i++;
      } else {
        nums1[m] = nums1[i];
        nums1[i] = nums2[j];
        i++;
        j++;
      }
    } else {
      while (nums1[m] <= nums2[j]) {
        if (nums1[m] <= nums1[i]) {
          nums1[m+1] = nums1[i];
          nums1[i] = nums1[m];
          m++;
          i++;
        }
      }

      if (nums2[j] < nums1[m] && nums2[j] < nums1[i]) {
        nums1[m+1] = nums1[i];
        nums1[i] = nums2[j];
        j++;
        m++;
        i++;
      }
    }
  }

  console.log(nums1);
};


merge([1,2,3,5,9,10,0,0,0], 6, [4,5,6], 3);
