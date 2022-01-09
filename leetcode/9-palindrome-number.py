#link:https://leetcode.com/problems/palindrome-number/
#id:9

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = str(x)
        
        # 1000021
          
        lengthN = len(n)
        expected = lengthN//2
        count = 0
        
        for i in range(lengthN):
            
            if count == expected:
                return True
            
            index = (lengthN - 1) - i
            if n[i] == n[index] and i < expected:
                count = count + 1
            
        return False
