from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int: 
        counter = [0, 0]
        max_count = 0
        left = 0
        for right in range(len(A)):
            counter[A[right]] += 1
            while counter[0] > K:
                counter[left] -= 1
                left += 1
            max_count = max(max_count, sum(counter))

        return max_count
        


# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         max_len = 0
#         start = 0
#         end = 0
#         k_count = K
#         cur_len = 0

#         while end < len(A):
#             if A[end] == 1:
#                 cur_len += 1
#                 if cur_len >= max_len:
#                     max_len = cur_len
#                 end += 1
#             elif A[end] == 0 and k_count > 0:
#                 cur_len += 1
#                 k_count -= 1
#                 end += 1
#                 if cur_len >= max_len:
#                     max_len = cur_len
                
#             elif A[end] == 0 and k_count <= 0:
#                 if A[start] == 0:
#                     start += 1
#                     k_count -= 1 
                
#                 cur_len -= 1
#                 end += 1

#         return max_len


        # max_len = 0
        # start = 0
        # end = start
        # current_len = 0
        
        # while end < len(A):
        #     if A[end] == 1:
        #         current_len += 1
        #         if current_len > max_len:
        #             max_len = current_len
        #     else:
        #         current_len = 0
        #         start = end
        #     end += 1

        # return max_len


x = Solution()
print(x.longestOnes([1,0,0,1,1,1,0,0,1,1,1,1,1,0,0], 1))
print(x.longestOnes([0], 1))
print(x.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(x.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))


