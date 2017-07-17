# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB : return None
        
        '''This method is much simpler than finding out the lengths of both the lists.'''
        '''Just traverse both the lists till one of them reaches the end, and then traverse the other one till it reaches the end.'''
        '''As a result both the lists will be at the same level and then comparisions of corresponding elements can be made.'''
        
        curra = headA
        currb = headB
        
        while curra and currb :
            curra = curra.next
            currb = currb.next
        
        while curra :
            curra = curra.next
            headA = headA.next
        
        while currb :
            currb = currb.next
            headB = headB.next
            
        while headA and headB :
            if headA == headB :
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
        
            
            
        
            
