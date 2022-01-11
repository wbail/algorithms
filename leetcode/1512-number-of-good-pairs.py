#link:https://leetcode.com/problems/number-of-good-pairs/
#id:1512

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                
                if nums[i] == nums[j] and i < j:
                    count = count + 1
            
        return count
