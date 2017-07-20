# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        ans = []
        final = []
        parent = [root]
        children = []
        
        while parent :
            for p in parent :
                if p :
                    ans.append(p.val)
                    children.append(p.left)
                    children.append(p.right)
            if ans :
                final.append(sum(ans)/float(len(ans)))
            parent = children
            children = []
            ans = []
        return final
                
        
