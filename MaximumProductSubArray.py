class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maximum = minimum = pro = nums[0]
        
        for i in range(1, len(nums)) :
            if nums[i] < 0 :
                maximum, minimum = minimum, maximum
                
            maximum = max(nums[i], maximum * nums[i])
            minimum = min(nums[i], minimum * nums[i])
    
            pro = max(pro, maximum)
            
        return pro
        
        
