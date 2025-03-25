
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storedNums = {}
    
        for i , num in enumerate(nums):
            difference = target - num
            if difference in storedNums:
                return [storedNums[difference], i]
            storedNums[num] = i
        


    
            
