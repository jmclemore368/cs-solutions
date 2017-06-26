# https://leetcode.com/problems/nested-list-weight-sum/


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.depthSumUtil(nestedList, 1, 0)
    
    
    def depthSumUtil(self, nestedList, multiplier, sum):
        for i, x in enumerate(nestedList):
            if x.isInteger():
                sum += x.getInteger() * multiplier
            else:
                sum += self.depthSumUtil(x.getList(), multiplier + 1, 0)
        return sum
        
        
        
        
        
        
        
        
        
