# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i, n in enumerate(nums):
            # Look for the complement
            if not target - n in mapping:
                mapping[n] = i
            else:
                return [mapping[target - n], i]
