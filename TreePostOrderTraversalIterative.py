# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''Doing pre order traversal on the mirror image of the given tree, results in the post order traversal of the given tree'''
        
        final = []
        stack = []
        
        while root or stack :
            if root :
                final.append(root.val)
                stack.append(root)
                root = root.right
            else :
                top = stack.pop()
                root = top.left
        return final[::-1]
