class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not len(nums) :
            return 
        curr_sum = final = nums[0]
        
        for i in range(1,len(nums)) :
            curr_sum = max(curr_sum+nums[i], nums[i])
            
            final = max(final, curr_sum)
        
        return final
        
