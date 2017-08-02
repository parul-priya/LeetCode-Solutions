# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : return head
        o = one = head
        e = even = head.next
        
        while one.next and one.next.next :
            one.next = one.next.next
            one = one.next
            even.next = even.next.next
            even = even.next
        
        one.next = e
        return head
