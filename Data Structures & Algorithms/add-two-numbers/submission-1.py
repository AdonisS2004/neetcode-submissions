# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get node vals
        n1, n2 = 0, 0
        node = l1
        while node:
            node = node.next
            n1 += 1
        node = l2
        while node:
            node = node.next
            n2 += 1

        # set A to the longest one
        A, B, nA, nB = None, None, 0, 0
        if n1 > n2:
            A, B = l1, l2
            nA, nB = n1, n2
        else:
            A, B = l2, l1
            nA, nB = n2, n1
        
        # do the math
        prev, nodeA, nodeB = None,A, B
        carry = 0
        while nodeA and nodeB:
            nodeSum = nodeA.val + nodeB.val + carry
            digit, carry = nodeSum % 10, nodeSum//10
            nodeA.val = digit
            prev = nodeA
            nodeA, nodeB = nodeA.next, nodeB.next
        
        # handle leftover carry
        while carry:
            if nodeA:
                nodeSum = nodeA.val + carry
                digit, carry = nodeSum % 10, nodeSum // 10
                nodeA.val = digit
                prev, nodeA = nodeA, nodeA.next
            else: 
                prev.next = ListNode(carry)
                carry = 0
        return A
