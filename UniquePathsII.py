class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        final = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        #Just need to check in the first row and first column, and also if the current cell is an obstacle.
        
        for i in range(len(grid[0]) ):
            if grid[0][i] == 1 :
                final[0][i] == 0
            else :
                if i==0 :
                    final[0][i] = 1
                else : final[0][i] = final[0][i-1]
        
        for i in range(1, len(grid)) :
            if grid[i][0] == 1 :
                final[i][0] = 0
            else : final[i][0] = final[i-1][0]
            for j in range(1, len(grid[0])) :
                if grid[i][j] and grid[i][j] :
                    final[i][j] = 0
                else :
                    final[i][j] = final[i-1][j] + final[i][j-1]
             
        return final[-1][-1]
                    
