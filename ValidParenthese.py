class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 : return False
        
        closed = set((")","}", "]"))
        pairs = set((("(", ")"),("[", "]") , ("{", "}")))
        ans = [s[0]]
        
        for i in s[1:] : 
            if i not in closed :
                ans.append(i)
                
            else :
                last = ans.pop()
                if (last, i) not in pairs  :
                        return False
        return not ans
