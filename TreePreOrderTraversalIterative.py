# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final = []
        stack = []
        
        while root or stack :
            if root :
                final.append(root.val)
                stack.append(root)
                root = root.left
            
            else :
                top = stack.pop()
                root = top.right
        return final
