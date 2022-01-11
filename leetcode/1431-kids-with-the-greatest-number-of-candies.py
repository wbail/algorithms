#link:https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
#id:1431

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # verify the highest number in the array
        
        # sum the extraCandies by each i
        
        # check if this sum is greater or equal
        
        # if yes: true
        # otherwise false
        
        higher = max(candies)
        result = []
        
        for i in range(len(candies)):
            
            sumCandies = candies[i] + extraCandies
            
            if sumCandies >= higher:
                result.append(True)
            else:
                result.append(False)
            
        return result
