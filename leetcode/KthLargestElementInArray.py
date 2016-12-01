# https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Keep min heap of exactly size k
        # Initialize all elements to -infinity
        h = [-sys.maxint - 1] * k
        
        for element in nums:
            root = h[0]  # Min element
            
            if element > root:  
                # Pop head, push element
                heapq.heapreplace(h, element)   
                
        return h[0]
            
