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
            
        result = []
        for word in words:
            reverse_word = word[::-1]
            
            # If Reverse(word) exists, then word + Reverse(word) makes a palindrome.
            if reverse_word in mapping:
                if mapping[reverse_word] != mapping[word]:  
                    result.append([mapping[word], mapping[reverse_word]])
                
            # If word is a palindrome and "" exists, then "" + word and word + "" are palindromes.
            if self.isPalindrome(word) and "" in mapping:
                if mapping[""] != mapping[word]:
                    result.append([mapping[word], mapping[""]])
                    result.append([mapping[""], mapping[word]])
                        
            # Check every combination of substrings in word.
            for i in range(1, len(word)):
                lhs = word[:i]
                rhs = word[i:]
                reverse_lhs = lhs[::-1]
                reverse_rhs = rhs[::-1]
                
                # If LHS is a palindrome and Reverse(RHS) exists, then Reverse(RHS) + word makes a palindrome.
                if self.isPalindrome(lhs) and reverse_rhs in mapping:
                    if mapping[reverse_rhs] != mapping[word]:
                        result.append([mapping[reverse_rhs], mapping[word]])
                    
                # If RHS is a palindrome and Reverse(LHS) exists, then word + Reverse(LHS) makes a palindrome.
                if self.isPalindrome(rhs) and reverse_lhs in mapping:
                    if mapping[reverse_lhs] != mapping[word]:
                        result.append([mapping[word], mapping[reverse_lhs]]) 
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
