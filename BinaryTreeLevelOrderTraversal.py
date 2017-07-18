# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        r = []
        parent = [root]
        children = []
        
        if not root : return result
        
        while parent :
            for p in parent :
                if p :
                    r.append(p.val)
                    children.append(p.left)
                    children.append(p.right)
            if r : 
                result.append(r)
            parent = children
            children = []
            r = []
        return result
