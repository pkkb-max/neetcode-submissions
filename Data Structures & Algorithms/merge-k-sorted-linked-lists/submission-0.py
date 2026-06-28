# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res

        while True:
            nextIndex = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if nextIndex == -1:
                    nextIndex = i
                if lists[nextIndex].val > lists[i].val:
                    nextIndex = i

            if nextIndex == -1:
                break
            cur.next = lists[nextIndex]
            lists[nextIndex] = lists[nextIndex].next
            cur = cur.next

        return res.next