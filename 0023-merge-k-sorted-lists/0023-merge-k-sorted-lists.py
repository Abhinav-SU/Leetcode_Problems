# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i , node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        dummy = ListNode(0)
        current = dummy
        
        # 2. PROCESS HEAP
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Link the node to our result
            current.next = node
            current = current.next
            
            # Push the NEXT node from the same list into heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next