# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0 : return head
        
        first = last = head
        l = 0
        
        while l < k and last.next :
            last = last.next
            l += 1
        
        if l == k :
            while last.next:
                last = last.next
                first = first.next
            final = first.next
            last.next = head
            first.next = None
            return final
        return self.rotateRight(head, k%(l+1))
        
