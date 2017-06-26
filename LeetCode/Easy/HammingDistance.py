# https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        result = 0
        while x != 0 or y != 0:
            xbit = x & 1
            ybit = y & 1
            result += (xbit ^ ybit)
            x >>= 1
            y >>= 1
        return result
            
