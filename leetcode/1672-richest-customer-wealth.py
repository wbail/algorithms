#link:https://leetcode.com/problems/richest-customer-wealth/
#id:1672

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        result = 0
        count = 0
        
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):

                count = count + accounts[i][j]
                
            if count > result:
                result = count
                
            count = 0
                
        return result
        