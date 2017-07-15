def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = []
        ans = []
        for i in range(len(nums)) :
            tar = target - nums[i]
            if tar in seen :
                ans.append(nums.index(tar))
                ans.append(i)
                return ans
            seen.append(nums[i])
