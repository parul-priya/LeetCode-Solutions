class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf") for i in range(n+1)]
        dp[1] = 1
        perfect = [1]
        for i in range(2,n+1) :
            if not i**0.5 - int(i**0.5) :
                dp[i] = 1
                perfect.append(i)
            else :            '''we are using only perfect squares here becaue the number i has to be sum of perfect squares only!'''
                for j in perfect :
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]
         
       
