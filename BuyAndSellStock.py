class Solution(object):
    def maxProfit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        buy = 0
        profit = 0

        '''for each incoming entry, check the profit and update the buy index'''
        for i in range(1,len(nums)) :
            profit = max(profit, nums[i]-nums[buy])
            if nums[i] < nums[buy] :
                buy = i
                
        return profit
