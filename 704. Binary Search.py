from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1

            else:
                return mid
        return -1
    
sol = Solution()

print(sol.search([-1,0,3,5,9,12], target= 9))
        
        
        
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4