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
    public ListNode mergeKLists(ListNode[] lists) {
        int amount = lists.length;
        int interval = 1;

        while( interval < amount ){
            for(int i=0; i<amount-interval; i+=interval*2){
                lists[i]=merge2Lists(lists[i],lists[i+interval]);
            }
            interval *= 2;
        }
        return amount > 0 ? lists[0] : null;
    }

    public ListNode merge2Lists(ListNode list1, ListNode list2){
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;

        while(list1!= null && list2!= null){
            if(list1.val <= list2.val){
                tail.next =list1;
                list1=list1.next;
            }
            else{
                tail.next =list2;
                list2=list2.next;
            }
            tail =tail.next;
        }

        if(list1!=null){
            tail.next =list1;
        }
        if(list2!=null){
            tail.next =list2;
        }

        return dummy.next;
    }
}