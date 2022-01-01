#Link:https://leetcode.com/problems/concatenation-of-array/
#Id:1929

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        numsLength = len(nums)
        numsLengthDouble = numsLength * 2
        
        numsDuplicated = []     
        
        for i in range(numsLengthDouble):
            
            if i < numsLength:
                numsDuplicated.append(nums[i])
            elif i == numsLength:
                
                for j in range(numsLength):
                    numsDuplicated.append(nums[j])
            
        return numsDuplicated
