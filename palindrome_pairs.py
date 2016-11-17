https://leetcode.com/problems/palindrome-pairs/


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mapping = {}
        for i, word in enumerate(words):
            mapping[word] = i
            
        result = []
        for i, word in enumerate(words):
            # Edge case: Consider if the reverse of word is present - i.e., the pair (word, Reverse(word))
            if word[::-1] in mapping and mapping[word[::-1]] != i:
                result.append([i, mapping[word[::-1]]])
                
            # Edge case: Consider the empty string. ("", word) and (word, "") are pairs if word is a palindrome
            if "" in mapping and self.isPalindrome(word) and mapping[""] != i:
                result.append([i, mapping[""]])
                result.append([mapping[""], i])
                        
            # Check every combination of lhs and rhs
            for j in range(1, len(word)):
                lhs = word[:j]
                rhs = word[j:]
                
                # If LHS is a palindrome, then the string Reverse(RHS) + LHS + RHS makes a palindrome.
                if self.isPalindrome(lhs) and rhs[::-1] in mapping and mapping[rhs[::-1]] != i:
                    result.append([mapping[rhs[::-1]], i])
                    
                # If RHS is a palindrome, then the string LHS + RHS + Reverse(LHS) makes a palindrome.
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
