#link:https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
#id:2114

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        count = 0
        numberOfWords = 0
        
        for i in range(len(sentences)):
            
            numberOfWords = sentences[i].count(' ') + 1
            
            if numberOfWords > count:
                count = numberOfWords
            
        return count
            