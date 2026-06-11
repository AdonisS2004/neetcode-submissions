# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        head = None
        while list1 is not None or list2 is not None:
            node = ListNode()
            if list1 is None:
                node.val = list2.val
                list2 = list2.next
            elif list2 is None:
                node.val = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                node.val = list2.val
                list2 = list2.next
            else:
                node.val = list1.val
                list1 = list1.next
            if head is None: head = node
            if res is None: res = node
            else: 
                res.next = node
                res = res.next
        return head