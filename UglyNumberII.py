class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''the idea here is simple!
           we basically want multiples of the numbers[2,3,5]
           so just keep choosing the minimum of such numbers!'''
        
        two = three = five= 0  #referring to the indices of anray ans
        ans = [1]
        
        while n-1 :
            minimum = min(2*ans[two], 3*ans[three], 5*ans[five])
            ans.append(minimum)
            if ans[two]*2 == minimum :
                two += 1
            if  ans[three]*3 == minimum :
                three += 1
            if  ans[five]*5 == minimum :            
                five += 1
            n-=1
        return ans[-1]
