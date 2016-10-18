/* 
  @problem
  Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

  Example 1: Given words = ["bat", "tab", "cat"]
             Return [[0, 1], [1, 0]]
             The palindromes are ["battab", "tabbat"]
  Example 2: Given words = ["abcd", "dcba", "lls", "s", "sssll"]
             Return [[0, 1], [1, 0], [3, 2], [2, 4]]
             The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

  @solution
  
  1. Given a string S, consider all partitions of the string S into 2 pairs (LHS, RHS).
     For a string of length k, this gives k possible pairs.
       Ex] Given "abaab", we try ("", "abaab"), ("a", "baab"), ("ab", "aab"), ("aba", "ab"), ("abaa", "b")
      
  2. Note the following 2 possibilities:
       a. If LHS is a palindrome, then the string LHS + RHS + Reverse(LHS) makes a palindrome.
       b. If RHS is a palindrome, then the string Reverse(RHS) + LHS + RHS makes a paldindrome.

  Thus, the process is as follows:
    a. For each strings S, put Reverse(S) into a map. O(n)
    b. For each strings S, consider each of the k combinations of ways to parition S into 2 pairs. O(n*k)
    c. For each combination, check if we can make a palindrome. O(n*k*k)
*/


