# https://leetcode.com/problems/majority-element/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer–Moore majority vote algorithm
        major = nums[0]
        count = 0
        for elem in nums:
            if count == 0:
                major = elem
                count = 1
            elif elem == major:
                count += 1
            else:
                count -= 1
                
         # Problem guarantees majority element. Otherwise: check if count is > 0. If not, there is no majority.
        return major  
