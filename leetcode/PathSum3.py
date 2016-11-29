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
        prefix_sums[0] = 1
        return self.pathSumUtil(root, 0, sum, prefix_sums)
        
    def pathSumUtil(self, curr, sum, tar, prefix_sums):
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
