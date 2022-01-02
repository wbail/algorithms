#link:https://leetcode.com/problems/middle-of-the-linked-list/
#id:876

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return 0
        
        curr = head
        countList = 0
        
        while curr:

            countList = countList + 1
            
            curr = curr.next
        
        if countList == 1:
            return head
        
        if countList > 0:
            
            curr = head
            count = 0
            
            while curr:
            
                count = count + 1
                
                if count == countList//2:
                    head = curr.next
                    return head
            
                curr = curr.next
            