# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        
        def inorder(root, result) :
            if root :
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)
                
        inorder(root, result)
        
        return sorted(list(set(result))) == result

        
