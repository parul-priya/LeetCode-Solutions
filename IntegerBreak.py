class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        
        for j in range(2, n+1) :
            for i in range(1,j) :
                dp[j] = max(dp[j], max(i, dp[i]) * max((j-i), dp[j-i]))
        return dp[-1]
                
            
            
        
