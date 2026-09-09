# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # base cases:
        if not head:
            return False
        if not head.next:
            return False
        
        # slow and fast pointer search
        slow, fast = head, head.next
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return False