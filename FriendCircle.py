
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = 0
        def dfs(row) :
            for i, val in enumerate(M[row]) :
                if val :
                    if i not in seen :
                        seen.add(i)
                        dfs(i)
                        
        for row in range(len(M)) :
            if row not in seen :
                dfs(row)
                ans += 1
        return ans

                        
        