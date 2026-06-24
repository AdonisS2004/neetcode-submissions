# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        
        slow, fast = head, head.next
        while slow and fast:
            if slow == fast:
                return True
            
            # update slow
            slow = slow.next
            # update fast
            fast = fast.next
            if fast:
                fast = fast.next
        return False