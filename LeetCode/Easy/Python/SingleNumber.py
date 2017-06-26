# https://leetcode.com/problems/single-number/


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        XOR all the elements.To see why this works, consider the following:
        ACBCABD                                 # Given
        = A ^ C ^ B ^ C ^ A ^ B ^ D             # XOR all elements
        = A ^ A ^ B ^ B ^ C ^ C ^ D             # Rearrange as follows. 
        =  (A ^ A) ^ (B ^ B) ^ (C ^ C) ^ D      # Group like terms
        = 0 ^ 0 ^ 0 ^ D                         # All duplicates cancel
        = 0 ^ D 
        = D
        """
        result = 0
        for x in nums:
            result ^= x
        return result
