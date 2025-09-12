/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode tortoise = head;
        ListNode hare = head;

        while(hare!=null || hare.next!=null){
            tortoise = tortoise.next;
            hare = hare.next.next;
            if(tortoise == hare)
                break;
        }

        if(hare == null || hare.next == null)
            return null;
        
        hare = head;

        while(hare!=tortoise){
            hare=hare.next;
            tortoise=tortoise.next;
        }

        return tortoise;
    }
}