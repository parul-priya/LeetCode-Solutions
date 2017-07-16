class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        final = [[0 for i in range(len(grid[0])+1)] for j in range(len(grid)+1)]
        
            
        for i in range(1, len(grid)+1) :
            for j in range(1, len(grid[0])+1) :
                if i == 1 or j == 1 :
                    final[i][j] = grid[i-1][j-1] + max(final[i-1][j], final[i][j-1])
                else :
                    final[i][j] = grid[i-1][j-1] + min(final[i-1][j], final[i][j-1])
       
        return final[-1][-1]
                
