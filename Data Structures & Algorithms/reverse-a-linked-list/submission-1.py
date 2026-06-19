# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        node = head
        nextNode = node.next
        while nextNode:
            # node -> nextNode -> unknown
            tmp = nextNode.next
            nextNode.next = node
            if node == head:
                node.next = None
            node = nextNode
            nextNode = tmp
        return node