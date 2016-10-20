




/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        // Make a dummy head to keep track of the front of the list
        ListNode dummyHead = new ListNode(0);

        // For iterating
        ListNode iterator = dummyHead;
        
        // While neither are null
        int carry = 0;
        while (l1 != null || l2 != null) {
            int sum = carry;
            
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            iterator.next = new ListNode(sum % 10);
            carry = sum / 10;
            iterator = iterator.next;
        } 
        
        if (carry != 0) {
            iterator.next = new ListNode(carry);
        }
        
        // Return the reused list
        return dummyHead.next;
        
        
    }
}
