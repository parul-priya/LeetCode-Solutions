# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root : return []
        dic = {}
        stack = []
        ans = []
        while root or stack :
            if root :
                stack.append(root)
                root = root.left
            else :
                top = stack.pop()
                if top.val in dic:
                    dic[top.val] += 1
                else : 
                    dic[top.val] = 1
                root = top.right
        mode = max(dic.values())
        for key in dic :
            if dic[key] == mode:
                ans.append(key)
        return ans
        
