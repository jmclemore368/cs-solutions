# https://leetcode.com/problems/path-sum-iii/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        prefix_sums = {}
        prefix_sums[0] = 1 # Edge case: for when the tree contains only 1 node.
        return self.pathSumUtil(root, 0, sum, prefix_sums)
        
    def pathSumUtil(self, curr, sum, tar, prefix_sums):
        """
              10
             /  \
            5   -3
           / \    \
          3   2   11
         / \   \
        3  -2   1
        
        A prefix sum for a node is the sum of values from the root to that node.
        Consider some node C, and any other arbitrary node N that is on the path between the root and C.
        Then the (sum from C -> N) = (prefix sum of C) - (prefix sum of N)
        
        Rearranging, note the (prefix sum of N) = (prefix sum of C) - (sum from C -> N)
        Since we are searching for a specific target sum, then (sum from C -> N) = tar
        Thus, we see that (prefix sum of N) = (prefix sum of C) - tar
        
        The strategy is to keep track of all the prefix sums in a hash table. 
        Note that there may be multiple prefix sums that are equal, so we also keep track of frequencies.
        Noting the above, for every prefix sum P in the recursion, we check to see if P - tar exists in our table.
        If P - tar exists in the table, it implies there is some path(s) that sum to target.
        
        As an edge case, note that the recursion is calculated bottom-up.
        Thus we must be sure to remove (or decrement) the prefix sum P when we return since it is no longer in consideration. 

        """
        if curr is None:
            return 0
        
        # Update the prefix sum
        sum += curr.val

        # Get the number of paths which end at this node and sum to target
        num_paths_to_curr = prefix_sums.get(sum - tar, 0)
        
        # Update the map with the current sum
        prefix_sums[sum] = prefix_sums.get(sum, 0) + 1

        # Recurse on children ala post-order traversal.
        left = self.pathSumUtil(curr.left, sum, tar, prefix_sums)
        right = self.pathSumUtil(curr.right, sum, tar, prefix_sums)
        result = num_paths_to_curr + left + right 
        
        # Since recursion goes bottom-up, we will no longer use this sum. 
        # Thus, we must decrement its frequency. 
        prefix_sums[sum] -= 1
        
        return result

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
