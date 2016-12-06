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
          N ->  5   -3
               / \    \
        C ->  3   2   11
             / \   \
            3  -2   1
            
        Suppose we are looking for a sum tar = 8. The idea is similar to two-sum, using the concept of "prefix-sums".
        
        A prefix sum for a node is the sum of values from the root to that node.
        Consider some node C, and any other arbitrary node N that is on the path between the root and C.
        
        Note the following:
        (path sum from N -> C) = (prefix sum of C) - (prefix sum of N)
        (prefix sum of N) = (prefix sum of C) - (path sum from N -> C)           # Rearrange
        (prefix sum of N) = (prefix sum of C) - tar                              # We search for path sums that equal tar
        
        The strategy is to keep track of all the prefix sums for every node in a hash table.
        1. For every node C, check if (prefix sum of C) - tar exists.
        2. If it exists, then there must exist a node(s) N, such that the path sum from N -> C = tar

        Note that the recursion is calculated bottom-up. Thus, decrement the frequency of the prefix sum of C when returning. 
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
