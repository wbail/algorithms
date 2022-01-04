#link:https://leetcode.com/problems/remove-linked-list-elements/
#id:203

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
                
        # 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> 7
        # 1 -> 2 ------> 3
        
        while (head != None and head.val == val):
            head = head.next
        
        curr = head
        
        while (curr != None and curr.next != None):
            
            if (curr.next.val == val):
                curr.next = curr.next.next
            else:
                curr = curr.next
                    
        return head
