# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root : return 0
        
        #there are two cases :
        #The following code is for sum of the values of all the leaves.
        # if not root.left and not root.right :
        #     return root.val
        # return self.sumOfLeaves(root.left) + self.sumOfLeaves(root.right)
        
        #The following code deals with the asked question : sum of left leaves
        if root.left and not root.left.left and not root.left.right :
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        