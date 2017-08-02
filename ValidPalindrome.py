class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2 : return True
        s = ''.join([i for i in s if i.isalnum()]).lower()
        
        i = 0
        j = len(s) - 1
        
        while i < j :
            if s[i] != s[j] :
                return False
            i += 1
            j -= 1
        return True
