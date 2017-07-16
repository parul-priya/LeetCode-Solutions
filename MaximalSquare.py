class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix : return 0
        row = len(matrix)
        col = len(matrix[0])
        
        final = [[0 for i in range(1+col)] for j in range(1+row)]
        result = 0
        for i in range(row) :
            for j in range(col) :
                if matrix[i][j] == '1' :
                    final[i+1][j+1] = min(final[i][j+1], final[i+1][j], final[i][j]) + 1
                    result = max(result, final[i+1][j+1])
        return result*result
          
            
