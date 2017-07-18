# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q : return True   '''when both the roots are null, return True'''
        if not p or not q : return False    '''when any one of the roots is null, return False'''
                                            
        if p.val == q.val :                 '''else compare root values, and proceed accordingly'''
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

