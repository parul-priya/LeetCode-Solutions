class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(height) - 1
        final = 0
        
        while i < j :
            curr_area = (j-i) * min(height[i], height[j])
            
            if height[i] < height[j] :
                i += 1
            else : 
                j -= 1
            
            final = max(final, curr_area)
        return final
