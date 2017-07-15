class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        
        row = len(matrix)
        
        for i in range(row) :
            for j in range(i+1) :
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(row) :
            for j in range(row/2) :
                matrix[i][j], matrix[i][row-j-1] = matrix[i][row-j-1], matrix[i][j]
        
        
