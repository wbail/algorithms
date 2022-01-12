#link:https://leetcode.com/problems/smallest-index-with-equal-value/
#id:2957

class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = -1
        
        for i in range(len(nums)):
            
            if i % 10 == nums[i]:
                
                if result == -1:
                    
                    result = i
                
                elif result > i:
                    
                    result = i
        
        return result