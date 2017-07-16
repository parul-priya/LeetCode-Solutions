# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = dummy = ListNode(0)
        carry = 0
        while l1 or l2 :
            if not l1 : l1 = ListNode(0)
            elif not l2 : l2 = ListNode(0)
                
            ans.next = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val+ carry)/10
            
            l1 = l1.next
            l2 = l2.next
            ans = ans.next
            
        if carry : 
            ans.next = ListNode(1)
        return dummy.next
            
            
            
