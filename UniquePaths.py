class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        final = [[1 for i in range(n)] for j in range(m)]
        for i in range(1,m) :
            for j in range(1,n):
                final[i][j] = final[i-1][j] + final[i][j-1]
        
        return final[-1][-1]
            
        
        
        
