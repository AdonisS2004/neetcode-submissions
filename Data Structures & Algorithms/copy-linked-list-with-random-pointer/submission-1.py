"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodeMap = dict()
        node = head
        while node:
            copy = Node(node.val, None, None)
            nodeMap[node] = copy
            node = node.next
        
        node = head
        while node:
            copy = nodeMap[node]
            if node.next:
                copy.next = nodeMap[node.next]
            if node.random:
                copy.random = nodeMap[node.random]
            node = node.next
        return nodeMap[head]