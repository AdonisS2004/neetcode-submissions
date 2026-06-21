# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base cases
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1

        # initialize, iterators, a constant start, 
        # and the node we build from
        l1, l2 = list1, list2
        head = ListNode()
        node = head

        # build sorted array
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next

        # add remaining l1
        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next
        
        # add remaining l2
        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next
            
        return head.next