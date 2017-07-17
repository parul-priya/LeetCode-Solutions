# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        '''So basically we are trying to first find the position from where the reversal will begin'''
        '''And then start reversing till required'''
        
        if not head or not head.next or n == m : return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        '''Remember to find the value of k here only! We are reducing the value of m later in the code.'''
        k = n-m
        
        while m-1 :
            prev = prev.next
            m -= 1
            
        curr = prev.next
        one = prev
        two = curr
        
        while k+1 :
            nextnode = curr.next
            curr.next = prev
            
            prev, curr = curr, nextnode
            k -= 1
        one.next = prev
        two.next = curr
        
        return dummy.next
            
        
