#link:https://leetcode.com/problems/count-items-matching-a-rule/
#id:1773

"""
Runtime: 212 ms, faster than 53.21% of Python online submissions for Count Items Matching a Rule.
Memory Usage: 21.2 MB, less than 28.02% of Python online submissions for Count Items Matching a Rule.
"""

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        count = 0
        
        dic = {
            "type": 0,
            "color": 1,
            "name": 2,
        }
        
        keys = dic.keys()
        
        value = None
        
        for i in range(len(keys)):
            
            if keys[i] == ruleKey:
                value = dic[keys[i]]
                
        
        """
           type        color      name
           
        [["phone",    "blue",   "pixel"],
         ["computer", "silver", "lenovo"],
         ["phone",    "gold",   "iphone"]]
        
        """
            
        for i in range(len(items)):
            
            for j in range(len(items[i])):
                
                if j == value and items[i][j] == ruleValue:
                
                    #print(items[i][j])
                    count += 1
        
        return count
