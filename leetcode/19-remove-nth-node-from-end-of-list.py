#link:https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#id:19

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        curr = head
        
        countList = 0
        
        while curr:
            
            curr = curr.next
            
            countList = countList + 1
            
        if countList < 2:
            head = None
            return head
        
        else:

            # 1    2    3    4    5
            # 
            # 1 -> 2 -> 3 -> 4 -> 5
            #
            # 5    4    3    2    1
            
            if countList == n:
                head = head.next
                return head
            
            curr = head
            count = 0
            
            while curr:
                
                count = count + 1
                
                if countList - count == n:
                
                    tempNode = curr.next.next
                    curr.next = tempNode
                
                curr = curr.next
        
        return head