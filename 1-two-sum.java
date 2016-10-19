/* 
  @problem
  
  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  You may assume that each input would have exactly one solution.

  Example:
  Given nums = [2, 7, 11, 15], target = 9,

  Because nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
  
  @solution
  
  Key Insight:
    - Given T, we want to find arbitrary A and B such that T = A + B. Note that A = T - B.
    - Thus, for every arbitrary number B, we want to see if T - B exists in the nums[].
    - If T - B exists in the array, and since A = T - B, we know that A exists in nums[]/
    - Thus, if A and B both exist in nums[], and A + B = T then we have found the solution.
    
  Approach:
    1. For each element B in nums[], create the mapping B -> index.
    2. For each element B in nums[], check if T - B exists in the map. If so, then this element T - B must be A.
    3. Since T - B must be A and A + B = T, we found the two-sum. Return the indices of A and B.
  
  Edge cases:
    1. Consider when B and A are equal, like 6 = 3 + 3. Thus, make sure A and B are not the same element when checking the map.
       
  Complexity: 
    Time: O(n) since we iterate over each element at most twice.
    Space: O(n) since we create a mapping for each element.
*/

// Beats 54.04% as of 10/19/2016
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // The problem statement says there is exactly one solution
        int[] result = new int[2];
        
        // For each element B in nums[], create the mapping B -> index.
        Map<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            hm.put(nums[i], i);
        }
        
        // For each element B in nums[], check if T - B exists in the map. If so, then this element T - B must be A.
        for (int j = 0; j < nums.length; ++j) {
            int A; // Not found yet
            int B = nums[j]; 
            
           //  Since T - B must be A, and A + B = T, we found the two-sum. Return the indices of A and B.
            if (hm.containsKey(target-B)) {
                
                // Edge case: Make sure B and A are not the same element
                if ((A = hm.get(target-B)) != j) {
                    result[0] = j;  // Index of B
                    result[1] = A;  // Index of A
                    break;
                 }
            }
        }
        
        // Guaranteed to have exactly one solution, given the problem.
        return result;
        
    }
}
