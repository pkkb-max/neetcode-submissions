# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, head:ListNode):
        self.head = head
    def __lt__(self,other):
        return self.head.val < other.head.val
    
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res
        heap = []

        for sorted_list_head in lists:
            if sorted_list_head is not None:
                heapq.heappush(heap, Node(sorted_list_head))

        while heap:
            minnode = heapq.heappop(heap)
            curr.next = minnode.head
            curr = curr.next
            if minnode.head.next:
                heapq.heappush(heap, Node(minnode.head.next))
        return res.next