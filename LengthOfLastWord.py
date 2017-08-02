class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        words = s.split(' ')
        
        i = len(words) - 1
        while i >= 0:
            if words[i] == '' : 
                i -= 1
            else : return len(words[i])
        return 0
            