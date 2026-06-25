# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # length check
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        if n < k:
            return head

        prevGroup, currGroup, newHead = None, head, None
        prev, curr = None, head
        idx = 0
        currk = 0
        while curr and idx + k <= n:
            currk = 0
            while curr and currk < k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                currk += 1
                idx += 1
            if prevGroup:
                prevGroup.next = prev
                prevGroup = currGroup
                currGroup = curr
            else:
                prevGroup = currGroup
                currGroup = curr
                newHead = prev
        prevGroup.next = currGroup
        return newHead