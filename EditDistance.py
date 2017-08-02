class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''create a matrix'''
        '''we are basically creating (i,j) pairs'''
        '''these pairs basically mean that for i letters in first word and j letters in second, these many operations will be required'''
        if not word1 and not word2 :
            return 0
        ans = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
  
        
        for i in range(len(ans[0])) :
            ans[0][i] = i
            
        for i in range(len(ans)) :
            ans[i][0] = i
     
        
        for i in range(0, len(word1)) :
            for j in range(0, len(word2)) :
                if word1[i] == word2[j] :
                    ans[i+1][j+1] = ans[i][j]
                else :
                    ans[i+1][j+1] = 1 + min(ans[i][j+1], ans[i+1][j], ans[i][j])
       
        return ans[-1][-1]
              
        