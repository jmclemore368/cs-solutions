# https://leetcode.com/problems/intersection-of-two-arrays/


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        visited = set()
        result = []
        for num in nums2:
            if num in nums1 and num not in visited:
                visited.add(num)
                result.append(num)
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
