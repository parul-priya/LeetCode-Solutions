class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower() :
            return True
        
        for i in word[1:] :
            if i == i.upper() :
                return False
        return True