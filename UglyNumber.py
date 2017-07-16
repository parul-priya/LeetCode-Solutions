class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 : return False
    
        for d in [2,3,5] :
            while not num % d :
                num /= d
        
        return  num == 1
       
        
