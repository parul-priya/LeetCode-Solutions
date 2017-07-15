class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        
        mid = len(nums)/2
        
        if target == nums[mid] :
            return mid
        
        if len(nums)==1 :
            if target < nums[0] : return 0
            else : return 1
            
        
        elif target < nums[mid] :
            return self.searchInsert(nums[:mid], target)
        return mid + self.searchInsert(nums[mid:], target)
