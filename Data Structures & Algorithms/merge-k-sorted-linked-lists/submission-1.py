# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode()
        prev, curr = None, dummyHead
        while curr:
            found = False
            minVal = None
            idx = -1
            for i, llist in enumerate(lists):
                if llist:
                    found = True
                    if minVal is None:
                        minVal = llist.val
                        idx = i
                    elif llist.val < minVal:
                        minVal = llist.val
                        idx = i
            if found:
                curr.next = lists[idx]
                lists[idx] = lists[idx].next
            else:
                curr.next = None
            curr = curr.next
        return dummyHead.next

                        