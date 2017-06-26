# https://leetcode.com/problems/palindrome-permutation/


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Map frequency of characters
        counter = collections.Counter(s)
        
        # A palindrome is possible IFF at most 1 character appears with odd frequency
        num_odd_elems = 0
        for c in counter:
            if (counter[c] % 2) != 0:
                num_odd_elems += 1
        
        return num_odd_elems <= 1
                
