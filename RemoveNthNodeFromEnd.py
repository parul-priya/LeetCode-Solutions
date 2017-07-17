# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next  : return None
        
        prev = last = head
        
        while n :
            last = last.next
            n -= 1
            
        if not last :
            return head.next
        
        while last.next :
            last = last.next
            prev = prev.next
            
        prev.next = prev.next.next
        
        return head
            
            
