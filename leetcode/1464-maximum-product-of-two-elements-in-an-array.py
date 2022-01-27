#link:https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
#id:1464

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0
        aux = 0
        
        for i in range(len(nums)):
            
            for j in range(len(nums)):
            
                if i != j:
            
                    aux = (nums[i] - 1) * (nums[j] - 1)

                if aux > result:
                    result = aux
        
        return result