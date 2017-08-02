# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        parent = TreeNode(0)
        parent.left = root
        p, r = parent, root
        
        while r and r.val != key :
            p = r
            if r.val < key : 
                r = r.right
            else :
                r = r.left
        if not r :
            return root
        
        q = r.right
        q_parent = r
        
        if not q :
            if r == p.left :
                p.left = r.left
            else :
                p.right = r.left
        
        else : 
            while q.left :
                q_parent = q
                q = q.left
            r.val = q.val
            
            if q == q_parent.left :
                q_parent.left = q.right
            else :
                q_parent.right = q.right
        return parent.left
                
            
            
            
        
        
    
            