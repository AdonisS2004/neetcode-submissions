# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers, n nodes apart
        if not head:
            return head
        prev, l, r = None, head, head
        for _ in range(n):
            r = r.next
        while r:
            prev = l
            l = l.next
            r = r.next
        # l is the nth node from back
        # remove l.next from list
        if l == head:
            return l.next
        prev.next = l.next
        return head