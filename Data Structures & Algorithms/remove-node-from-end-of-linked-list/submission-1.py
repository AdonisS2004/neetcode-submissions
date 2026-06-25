# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        node = head
        while node:
            node = node.next
            sz += 1
        
        idx = 0
        prev, curr = None, head
        target = sz - n
        while idx < target:
            prev = curr
            curr = curr.next
            idx += 1
        
        if not prev:
            return curr.next
        prev.next = curr.next
        return head