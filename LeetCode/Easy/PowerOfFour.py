# https://leetcode.com/problems/power-of-four/


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        Condition I:
        Every multiple of 4 has exactly one bit set. I.e.,
        4 ^ 1 = 0000 0100
        4 ^ 2 = 0001 0000
        4 ^ 3 = 0100 0000
        Thus, x & (x - 1) should be 0.

        Condition II:
        Any power of 4 minus 1 is divisble by 3.
        1 - 1 = 0
        4 - 1 = 3
        16 - 1 = 15
        64 - 1 = 63
        
        Proof (Credits to user gaojianchao1991)
        1) 4^n - 1 = (2^n + 1) * (2^n - 1)
        2) among any 3 consecutive numbers, there must be one that is a multiple of 3
        3) Thus, among (2^n-1), (2^n), (2^n+1), one of them must be a multiple of 3
        4) (2^n) cannot be the one, therefore either (2^n-1) or (2^n+1) must be a multiple of 3,
        5) Since these are factors of 4^n-1, then 4^n-1 must be a multiple of 3 as well.
        """
        return num & (num - 1) == 0 and (num - 1) % 3 == 0
        

            
        
