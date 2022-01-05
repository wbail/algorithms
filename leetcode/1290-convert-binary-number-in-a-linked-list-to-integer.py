#link:https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
#id:1290

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        curr = head
        
        result = 0
        count = -1
        
        while curr:
            
            count = count + 1
            
            curr = curr.next
            
        curr = head
        
        while curr:
            
            result = result + (curr.val * pow(2, count))
            
            count = count - 1
            curr = curr.next
            
        return result