#link:https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#id:1295

"""
Runtime: 48 ms, faster than 41.10% of Python online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 13.4 MB, less than 83.98% of Python online submissions for Find Numbers with Even Number of Digits.
"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        result = 0
        
        for i in nums:
        
            while i > 0:
                i = i // 10
                count = count + 1
            
            if count % 2 == 0:
                
                result = result + 1
                
            count = 0
        
        return result