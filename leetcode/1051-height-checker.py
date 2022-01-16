#link:https://leetcode.com/problems/height-checker/
#id:1051

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        count = 0
        expected = []
        j = 1
        
        for i in range(len(heights)):
            
            expected.append(heights[i])
                
        for i in range(len(expected)):
            
            for j in range(len(expected)):
                
                if expected[j] > expected[i]:

                    aux = expected[i]

                    expected[i] = expected[j]

                    expected[j] = aux
        
        for i in range(len(heights)):
            
            if heights[i] != expected[i]:
                
                count = count + 1
                
        return count
