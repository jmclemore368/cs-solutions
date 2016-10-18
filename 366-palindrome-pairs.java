/* 
  @problem
  Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that 
  the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

  Example 1: Given words = ["bat", "tab", "cat"]
             Return [[0, 1], [1, 0]]
             The palindromes are ["battab", "tabbat"]
  Example 2: Given words = ["abcd", "dcba", "lls", "s", "sssll"]
             Return [[0, 1], [1, 0], [3, 2], [2, 4]]
             The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

  @solution
  
  1. Given a string S, consider all partitions of the string S into 2 pairs (LHS, RHS).
     For a string of length k, this gives k possible pairs.
       Ex] Given "abaab", consider ("", "abaab"), ("a", "baab"), ("ab", "aab"), ("aba", "ab"), ("abaa", "b")
      
  2. Note the following 2 possibilities:
       a. If RHS is a palindrome, then the string LHS + RHS + Reverse(LHS) makes a palindrome.
       b. If LHS is a palindrome, then the string Reverse(RHS) + LHS + RHS makes a paldindrome.

  Thus, the process is as follows:
    a. For each strings S, put Reverse(S) into a map. Use indices as the value, as we need them for the final answer.
    b. For each strings S, consider each of the k combinations of ways to parition S into 2 pairs. O(n*k)
    c. For each combination, check if we can make a palindrome. O(n*k*k)
*/


public class Solution {
    
  // Check if String is palindrome. 
  public static boolean isPalindrome(String s){
    for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
      if (s.charAt(i) != s.charAt(j)) {
        return false;
      }
    }
    // For this problem, consider the empty string as not a palindrome
    return s.isEmpty() ? false : true;  
  }
    
  // Utility function
  public static String reverseString(String s) {
    return new StringBuilder(s).reverse().toString();
  }
    
  // Solution
  public List<List<Integer>> palindromePairs(String[] words) {
    List<List<Integer>> result = new ArrayList<>();
        
    // For each strings S, put S -> Index into a map. 
    // Use indices as the value, as we need them for the final answer.
    Map<String, Integer> hm = new HashMap<>();
    for (int i = 0; i < words.length; ++i) {
      hm.put(words[i], i);
    }
        
    // For each strings S, consider each of the k combinations of ways to partition S into 2 pairs.
    // Edge cases: Be careful not to concatenate a string with itself
    Integer index;
    for (int i = 0; i < words.length; ++i) {

      // Edge case: Consider if the reverse of S is present. I.e., the pair (S, Reverse(S))
      if ((index = hm.get(reverseString(words[i]))) != null && index.intValue() != i) {
        result.add(Arrays.asList(new Integer[] {i, index}));
      }
            
      // Edge case: Consider the empty string. ("", S) and (S, "") is a palindrom IFF S is a palindrome.
      if ((index = hm.get("")) != null && index.intValue() != i) {
        if (isPalindrome(words[i])){
          result.add(Arrays.asList(new Integer[] {i, index}));
          result.add(Arrays.asList(new Integer[] {index, i}));
        }
      }
            
      // For each combination, check if we can make a palindrome.
      for (int j = 1; j < words[i].length(); ++j) {
                
        String LHS = words[i].substring(0,j);
        String RHS = words[i].substring(j);

        // If LHS is a palindrome, then the string Reverse(RHS) + LHS + RHS makes a palindrome.
        if (isPalindrome(LHS)){
          if ((index = hm.get(reverseString(RHS))) != null && index.intValue() != i) {
            result.add(Arrays.asList(new Integer[] {index, i}));
          }
        }
                
        // If RHS is a palindrome, then the string LHS + RHS + Reverse(LHS) makes a palindrome.
        if (isPalindrome(RHS)){
          if ((index = hm.get(reverseString(LHS))) != null && index.intValue() != i) {
            result.add(Arrays.asList(new Integer[] {i, index}));
          }
        }
      }
    }
        
    return result; 
    }
  }
