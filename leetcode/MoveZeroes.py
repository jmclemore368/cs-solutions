# https://leetcode.com/problems/move-zeroes/


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Parition according to the following loop invariants:
        # non-zero elements: nums[:p1]
        # zero elements: nums[p1:p2]
        # unclassified elements: nums[p2:]
        p1 = 0 
        p2 = 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
    
