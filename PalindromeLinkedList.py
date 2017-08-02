# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next : return True

        slow = head
        fast = head.next
        ans = [slow.val]
        
        while fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
            ans.append(slow.val)
        print 'ans', ans
        if not fast.next :
            two = slow.next
        else : 
            two = slow.next.next
        while ans :
            temp = ans.pop()
            if temp != two.val :
                return False
            else :
                two = two.next
        return True
        
