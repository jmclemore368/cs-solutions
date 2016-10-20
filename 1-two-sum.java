/* 
  https://leetcode.com/problems/two-sum/
  https://leetcode.com/articles/two-sum/
*/

// Beats 54.04% as of 10/19/2016
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // The problem statement says there is exactly one solution guaranteed.
        int[] result = new int[2];
        
        // For each element B in nums[], create the mapping B -> index.
        Map<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            hm.put(nums[i], i);
        }
        
        // For each element B in nums[], check if T - B exists.
        for (int j = 0; j < nums.length; ++j) {
            int A; // Not found yet
            int B = nums[j]; 
            
            // If T - B exists, then this element T - B must be A.
            if (hm.containsKey(target-B)) {
                
                // Edge case: Make sure B and A are not the same element
                if ((A = hm.get(target-B)) != j) {
                    
                    // Since T - B must be A, and A + B = T, we have found both A and B.
                    result[0] = j;  // Index of B
                    result[1] = A;  // Index of A
                    break;
                 }
            }
        }
      
        // Return the indices of A and B.
        return result;
        
    }
}
