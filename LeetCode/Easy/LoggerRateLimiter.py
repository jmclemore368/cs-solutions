# https://leetcode.com/problems/logger-rate-limiter/


class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if not message in self.map:
            self.map[message] = timestamp
            return True
        
        latest_time = self.map[message]
        if latest_time > timestamp - 10:
            return False
        else:
            # If latest_time is not printed in the last 10 seconds, then we are going to print it.
            # Therefore, we must update latest_time to reflect this.
            self.map[message] = timestamp
            return True
        
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
