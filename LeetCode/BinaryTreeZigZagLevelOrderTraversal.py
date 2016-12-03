# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        stack_one = []
        stack_two = []

        stack_one.append(root)
        while stack_one or stack_two:
            level = []
            while stack_one:
                top = stack_one.pop()
                if top:
                    level.append(top.val)
                    if top.left:
                        stack_two.append(top.left)
                    if top.right:
                        stack_two.append(top.right)
            if level:
                result.append(level)
            
            level = []
            while stack_two:
                top = stack_two.pop()
                if top:
                    level.append(top.val)
                    if top.right:
                        stack_one.append(top.right)
                    if top.left:
                        stack_one.append(top.left)
            if level:
                result.append(level)        
          
        return result
                        
    
                        
        
        
