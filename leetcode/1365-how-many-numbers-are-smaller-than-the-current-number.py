#link:https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#id:1365

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        count = 0
        numsLength = len(nums)
        result = []
        
        for i in range(numsLength):
            
            for j in range(numsLength):
                
                if nums[j] < nums[i]:
                    count = count + 1
            
            result.append(count)
            count = 0
            
        return result
            