# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next : return head
        
        head, head.next = ListNode(0), head
        dummy = head
        
        """To check if the upcoming entry has
                            already ocurred in the list
                       """
        copied = False 
        
        while head.next and head.next.next :
            if head.next.val == head.next.next.val :
                head.next = head.next.next
                copied = True
            elif copied :
                head.next = head.next.next
                copied = False
            else :
                head = head.next
        if copied :
            head.next = None
        return dummy.next
