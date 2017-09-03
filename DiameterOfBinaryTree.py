# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root : return 0
        
        ans = []
        stack = []
        while root or stack :
            if root : 
                stack.append(root)
                root = root.left
            else :
                root = stack.pop()
                ans.append(1 + self.depth(root.left) + self.depth(root.right))
                root = root.right
        return max(ans) - 1
        
    def depth(self, root) :
        if not root : return 0 
        return 1 + max(self.depth(root.left), self.depth(root.right))

    
    
    
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root : return 0
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left+right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
    def height(self, root) :
        if not root : return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
