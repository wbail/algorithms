#link:https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
#id:2011

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        result = 0
        
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                result = result -1
                
            elif operations[i] == "X++" or operations[i] == "++X":
                result = result + 1
                
        return result