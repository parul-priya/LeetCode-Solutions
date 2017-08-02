# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        curr = 0
        final = root
        while root or stack : 
            if root :
                stack.append(root)
                root = root.right
            else :
                top = stack.pop()
                curr += top.val
                top.val = curr
                root = top.left
        return final
