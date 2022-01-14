#link:https://leetcode.com/problems/single-number/
#id:136

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        
        if length == 1:
            return nums[0]
            
        count = 0
        result = 0

        for i in range(length):

            for j in range(length):

                if nums[i] == nums[j] and i != j:
                    
                    count = count + 1

            if count == 0:
                result = nums[i]
                
            count = 0
            
        return result
