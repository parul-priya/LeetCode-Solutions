class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.arr = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.arr.append(val)
        l = min(self.size, len(self.arr))
        
        return sum(self.arr[-(self.size):])/float(l)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)