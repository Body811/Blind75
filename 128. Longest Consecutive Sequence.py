from typing import List
from collections import defaultdict


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         dict = defaultdict(int)
#         for n in nums:
#             dict[n] += 1
            
#         for i in range(len(dict)):
#             print(dict[i])
                    
                    
                    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums):
            nums.sort()
            res = 1
            newmax = 1
            for i in range(len(nums)):
                if i > 0:
                    if (nums[i] - 1) == nums[i - 1]:
                        newmax += 1
                    elif (nums[i]) == nums[i - 1]:
                        continue
                    else:
                        res = max(newmax,res)
                        newmax = 0
            return max(res,newmax)
        else:
            return 0
            
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))