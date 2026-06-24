# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        l, r = head, head
        n = 0

        # count number of nodes
        while r:
            r = r.next
            n += 1

        # go to middle
        r = head
        count = 0
        while count < n//2:
            r = r.next
            count += 1
        
        # reverse the second half
        r_prev = None
        while r:
            tmp = r.next
            r.next = r_prev
            r_prev = r
            r = tmp
        r = r_prev

        # merge them one by one
        newHead = l
        while l and r:
            tmp_l = l.next
            tmp_r = r.next
            l.next = r
            r.next = tmp_l
            l = tmp_l
            r = tmp_r
        if l: l.next = None
