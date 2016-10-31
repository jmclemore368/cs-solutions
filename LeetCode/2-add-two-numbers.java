/*
   https://leetcode.com/problems/add-two-numbers/
   https://leetcode.com/articles/add-two-numbers/
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// Beats 55.12% as of 10/31/2016
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        // Use a dummyHead to simplify keeping track of the head of the list
        ListNode dummyHead = new ListNode(0);
        ListNode iterator = head;
        int sum = 0;

        while (l1 != null || l2 != null) {
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            iterator.next = new ListNode(sum % 10);
            sum = sum / 10;   // Carry
            iterator = iterator.next;
        }

        // If there's a carry
        if (sum != 0) {
            iterator.next = new ListNode(sum);
        }

        return dummyHead.next;
    }
}
