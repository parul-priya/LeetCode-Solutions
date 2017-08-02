class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s : return ''
        if len(s) == 1 : return s
        else :
            return self.reverseString(s[len(s)/2 : ]) + self.reverseString(s[ : len(s)/2])
        
