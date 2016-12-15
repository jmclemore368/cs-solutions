# https://leetcode.com/problems/merge-sorted-array/


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        
        # Fill in from back to front, using 3 pointers
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                nums1[p3 - 1] = nums2[p2]
                p1 -= 1
                p2 -= 1
                p3 -= 1
            p3 -= 1   
          
        # If nums2 has more elements, fill them into the remainder of the array
        if p2 >= 0:
            while p2 >= 0:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1
        
        
        
        
        
