class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        
        if len(x) == 0 : return True
        if x[0] != x[-1] : return False
        return self.isPalindrome(x[1:-1])
        
