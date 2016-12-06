# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = list()
        s_counter = Counter(s[:len(p) - 1])
        p_counter = Counter(p)

        # Maintain a window of len(p) in s, and slide to right until finish. 
        for i in range(len(p) - 1, len(s)):
            
            # Include a new char in the sliding window
            s_counter[s[i]] += 1
            
            # The comparison is O(1), since there are at most 26 letters in the alphabet
            if s_counter == p_counter:
                result.append(i - len(p) + 1)
                
            # Remove oldest char in the sliding window. Delete it if count goes to 0.
            s_counter[s[i - len(p) + 1]] -= 1
            if not s_counter[s[i - len(p) + 1]]:
                del s_counter[s[i - len(p) + 1]]

        return result
    
            
                

              
            
                
            
            
                
                
                
            
            
