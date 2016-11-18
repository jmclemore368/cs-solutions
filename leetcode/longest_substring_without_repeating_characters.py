https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        p2 = 0
        p1 = 0
        largest_len = 0
        while p1 < len(s):
            char = s[p1]
            if char in mapping and mapping[char] >= p2:
                p2 = mapping[char] + 1
            mapping[char] = p1
            largest_len = max(largest_len, p1 - p2 + 1)
            p1 += 1
        return largest_len
  
            

                
