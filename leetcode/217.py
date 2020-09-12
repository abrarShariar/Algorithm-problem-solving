class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if (dict.get(nums[i], -1) != -1):
                return True
                
            dict[nums[i]] = i
        return False
    