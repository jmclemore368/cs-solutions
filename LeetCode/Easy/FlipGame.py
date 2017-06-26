# https://leetcode.com/problems/flip-game/


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = [str(c) for c in s]     # Use list comprehension and str() to strip unicode characters
        result = []
        i = 0
        while i < len(s) - 1:
            if s[i] == '+' and s[i + 1] == '+':
                flip = s[:i] + ['-', '-'] + s[i + 2:]
                result.append(''.join(flip))
            i += 1
        return result
  
     
                
            
            
                
        
        
        
