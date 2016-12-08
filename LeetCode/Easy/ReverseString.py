# https://leetcode.com/problems/reverse-string/


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert to list first as strings are immutable
        s_list = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]  # swap
            i += 1
            j -= 1
        return ''.join(s_list)
