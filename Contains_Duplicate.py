
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
    
#Another solution 
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False if len(set(nums)) == len(nums) else True 
    
        