class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums : return 0
        elif len(nums) == 1 : return nums[0]
            
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums) :
        if not nums :
            return
        elif len(nums) == 1 :
            return nums[0]
        
        h1 = nums[0]
        h2 = final = max(nums[0], nums[1])
        
        for i in range(2, len(nums)) :
            final = max(final, nums[i] + h1)
            
            h1, h2 = h2, final
        return final
