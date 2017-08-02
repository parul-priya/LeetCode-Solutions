# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        child = [root]
        parent = []
        while child:
            parent = child
            child = [ kid for node in child for kid in (node.left, node.right) if kid is not None ]
        return parent[0].val