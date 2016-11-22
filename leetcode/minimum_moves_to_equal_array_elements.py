# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        smallest_element = min(nums)

        # The number of moves is the sum of all Xi - smallest_element
        # I.e., given [1, 2, 3], the smallest is 1.
        # The sum is (1-1) + (2-1) + (3-1) = 3
        num_moves = sum(num - smallest_element for num in nums)
        return num_moves
         
