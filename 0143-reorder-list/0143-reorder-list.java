/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return; // Edge case: empty or single-node list

        // Step 1: Find middle of the list
        ListNode slow = head, fast = head, prev = null;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        if (prev != null) prev.next = null; // Break the list into two parts

        // Step 2: Reverse the second half
        ListNode l2 = reverse(slow);
        
        // Step 3: Merge two halves
        mergeList(head, l2);
    }

    public ListNode reverse(ListNode head) {
        ListNode prev = null, curr = head;
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        return prev; // New head of reversed list
    }

    public void mergeList(ListNode l1, ListNode l2) {
        while (l1 != null && l2 != null) {
            ListNode l1_next = l1.next;
            ListNode l2_next = l2.next;

            l1.next = l2;
            if (l1_next == null) break; // If the first list is shorter, stop merging

            l2.next = l1_next;
            l1 = l1_next;
            l2 = l2_next;
        }
    }
}
