# SOLVED!
class Solution:
    def intersect(self, nums1, nums2):
        nums1_map, nums2_map = {}, {}
        result_list = []

        for num in nums1:
            nums1_map[num] = nums1_map.get(num, 0) + 1

        for num in nums2:
            nums2_map[num] = nums2_map.get(num, 0) + 1

        for key in nums1_map.keys():
            if nums2_map.get(key, None):
                num_count = min(nums1_map[key], nums2_map[key])
                result_list += [key] * num_count

        return result_list

