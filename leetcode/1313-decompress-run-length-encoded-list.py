#link:https://leetcode.com/problems/decompress-run-length-encoded-list/
#id:1313

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        
        for i in range(len(nums)-1):
            
            if i % 2 == 0:
                for j in range(nums[i]):
                    result.append(nums[i+1])
                    
        return result
