import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''for each incoming letter, either it is already there in the answer or not.'''
        '''if it is there in the answer already, there is no need to check the maximum. It will either be the same or less than this if the             incoming letter is included'''
        '''hence check for max only when the letter is not already present in the answer'''
        
        if not s : return 0
        
        start = 0
        max_len = 0
        let_pos = {}
        
        for i in range(len(s)) :
            if s[i] in let_pos and start <= let_pos[s[i]] :
                start = let_pos[s[i]] + 1
            else :
                max_len = max(max_len, i - start + 1)
            let_pos[s[i]] = i
        return max_len