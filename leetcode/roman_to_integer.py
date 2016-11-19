https://leetcode.com/problems/roman-to-integer/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        sum = mapping[s[len(s) - 1]]  # Add last char
        i = len(s) - 2
        while i >= 0:
            # Rule: Placing a smaller number in front of a larger number means subtraction.
            # I.e., IV means V - I = 5 - 1 = 4; whereas VI means V + I = 5 + 1 = 6
            if mapping[s[i]] < mapping[s[i + 1]]:
                sum -= mapping[s[i]]
            else:
                sum += mapping[s[i]]
            i -= 1
        return sum
            
            
            
                   
