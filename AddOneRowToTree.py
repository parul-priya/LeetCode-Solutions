# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1 : 
            root, root.left = TreeNode(v), root
        else :
            lis = self.findList(root, d)
            for node in lis :
                node.left, node.right, node.left.left, node.right.right = TreeNode(v), TreeNode(v), node.left, node.right
        return root
    
    def findList(self, root, d) :
        if root :
            ans = []
            if d == 2 :
                ans.append(root)
            else :
                ans += self.findList(root.left, d-1)
                ans += self.findList(root.right, d-1)
            return ans
        return [TreeNode(None)]
    
