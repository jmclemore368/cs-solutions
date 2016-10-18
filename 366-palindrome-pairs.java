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
  
  Key Insight:
    * Given a string S, consider all partitions of the string S into 2 pairs (LHS, RHS).
    * For a string of length k, this gives k-1 possible pairs.
       Ex] Given "abaab", consider ("a", "baab"), ("ab", "aab"), ("aba", "ab"), ("abaa", "b")
    * Note how the following holds true:
       a. If RHS is a palindrome, then the string LHS + RHS + Reverse(LHS) makes a palindrome.
       b. If LHS is a palindrome, then the string Reverse(RHS) + LHS + RHS makes a palindrome.

  Approach:
    1. For each string S in A[], create the mapping S -> index.
    2. For each string S, consider each of the k combinations of ways to parition S into 2 pairs. 
    3. For each combination, check if we can make a palindrome using the above logic.
   
  Edges cases:
    1. Consider if Reverse(S) is present. I.e., the pair (S, Reverse(S)).
      * Thus, contrary to what we said earlier, for a string of length k, there are actually exactly k possible pairs
    2. Consider the empty string. The pairs ("", S) and (S, "") are palindromes if and only if S is a palindrome.
    3. Do not concatenate S with itself. Check that Reverse(S) and S have distinct indices (assumes no duplicates).
    
  Complexity: 
    Given n strings, we iterate over each string S, giving O(n).
    For each S, we check all k combinations for palindromicity, giving O(n*k).
    Since checking for palindromicity takes O(k), this gives total time O(n*k*k).
*/


/* Beats 81.21% as of 10/18/2016 */
public class Solution {
    
  // Check if String is palindrome. 
  public static boolean isPalindrome(String s){
    for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
      if (s.charAt(i) != s.charAt(j)) {
        return false;
      }
    }
    return true;  
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
    // Edge cases: Do not concatenate S with itself. Check that Reverse(S) and S have distinct indices.
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
