class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s : return 0
        if not int(s[0])  : return 0
       
        dp = [1 for i in range(len(s)+1)]
        test = s[0]
        
        for i in range(2, len(s)+1) :
            
            test = test[-1] + s[i-1]
            t = int(test)
          
            if not t % 10 : 
                if not t or t / 10 >= 3:
                    return 0
                else :
                    dp[i] = dp[i-2]
            elif t > 26 or t < 10:
                dp[i] = dp[i-1]
                
            else : dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
    
            
