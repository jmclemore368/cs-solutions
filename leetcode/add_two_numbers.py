# https://leetcode.com/submissions/detail/82971652/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        current = dummy_head
        p1 = l1
        p2 = l2
        sum = 0
        while p1 or p2:
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            current.next = ListNode(sum % 10)
            sum /= 10
            current = current.next

        if sum:
            current.next = ListNode(sum)
        return dummy_head.next
        
