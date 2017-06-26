# https://leetcode.com/problems/moving-average-from-data-stream/


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.deque = collections.deque()
        self.max_size = size
        self.moving_total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.deque) >= self.max_size:
            oldest = self.deque.popleft()
            self.moving_total -= oldest
        self.deque.append(val)
        self.moving_total += val
        return self.moving_total / float(len(self.deque))
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
