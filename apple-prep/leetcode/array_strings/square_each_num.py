class Solution:
    def sortedSquares(self, nums):
        return sorted(list(map(lambda x: x**2, nums)))