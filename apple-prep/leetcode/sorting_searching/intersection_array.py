# SOLVED!
class Solution:
    def intersection(self, nums1, nums2):
        result_list = []
        num1_map = {}
        num2_map = {}
        for num in nums1:
            num1_map[num] = 1
        for num in nums2:
            num2_map[num] = 1

        for key in num1_map.keys():
            if num2_map.get(key, None):
                result_list.append(key)

        return result_list