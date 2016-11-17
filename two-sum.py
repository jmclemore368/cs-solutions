# https://leetcode.com/problems/two-sum/
# Beats 96.40% of Python submissions as of 11/17/2016


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = {}
        for i, n in enumerate(nums):
            if not target - n in pairs:
                pairs[n] = i
            else:
                return [pairs[target - n], i]
