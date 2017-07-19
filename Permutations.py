class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) == 0 or len(nums) == 1 : return [nums]  #since ans is list of list, so this should also be list of lists
        
        for i in range(len(nums)) : 
            for j in self.permute(nums[:i] + nums[i+1:]):
                sub = [nums[i]] + j
                ans.append(sub)
        return ans                         #ans is list of lists
