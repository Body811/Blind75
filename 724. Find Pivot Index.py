from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, n in enumerate(nums):
            
            if(leftsum == total - leftsum - n):
                return i
            else:
                leftsum += n
                
        return -1
            
          

          