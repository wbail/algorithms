#link:https://leetcode.com/problems/sum-of-unique-elements/
#id:1748

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        result = 0
        
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                
                if i != j and nums[i] == nums[j]:
                    
                    count += 1
                    
            if count == 0:
                result = result + nums[i]
            
            count = 0
            
        return result
