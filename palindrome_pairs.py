# https://leetcode.com/problems/palindrome-pairs/


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mapping = {}
        for i, word in enumerate(words):
            mapping[word] = i
            
        # Edge case: Make sure that indices are distinct when checking.
        result = []
        for i, word in enumerate(words):
            
            # Edge case: Consider if Reverse(word) exists.
            # Then word + Reverse(word) makes a palindrome.
            if word[::-1] in mapping and mapping[word[::-1]] != i:
                result.append([i, mapping[word[::-1]]])
                
            # Edge case: Consider if empty string exists.
            # Then "" + word and word + "" make palindromes.
            if "" in mapping and self.isPalindrome(word) and mapping[""] != i:
                result.append([i, mapping[""]])
                result.append([mapping[""], i])
                        
            # Check every combination of substrings in word.
            for j in range(1, len(word)):
                # Let word be given by LHS + RHS
                lhs = word[:j]
                rhs = word[j:]
                
                # Consider if LHS is a palindrome and Reverse(RHS) exists.
                # Then Reverse(RHS) + word makes a palindrome.
                if self.isPalindrome(lhs) and rhs[::-1] in mapping and mapping[rhs[::-1]] != i:
                    result.append([mapping[rhs[::-1]], i])
                    
                # Consider if RHS is a palindrome and Reverse(LHS) exists.
                # Then word + Reverse(LHS) makes a palindrome.
                if self.isPalindrome(rhs) and lhs[::-1] in mapping and mapping[lhs[::-1]] != i:
                    result.append([i, mapping[lhs[::-1]]]) 
        return result
                        
    def isPalindrome(self, word):
        i = 0
        j = len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
