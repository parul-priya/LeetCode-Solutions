class Solution(object):
    def canConstruct(self, s, m):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in s :
            if i in dic1 : 
                dic1[i] += 1
            else :
                dic1[i] = 1
        
        for i in m : 
            if i in dic2 : 
                dic2[i] += 1
            else :
                dic2[i] = 1
        
        for key in dic1 :
            if key not in dic2 :
                return False
            else :
                if dic1[key] > dic2[key]:
                    return False
        return True