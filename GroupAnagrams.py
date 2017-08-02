class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        
        for s in strs :
            base = ''.join(sorted(s))
            if base not in dic:
                dic[base] = [s]
            else :
                dic[base].append(s)
        
        return dic.values()
