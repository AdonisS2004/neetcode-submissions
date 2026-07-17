"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copy_map = dict()
        def copy(new, old):
            new.val = old.val
            copy_map[old] = new
            for neighbor in old.neighbors:
                if neighbor not in copy_map:
                    copy(Node(), neighbor)
                new.neighbors.append(copy_map[neighbor])
        new = Node()
        copy(new, node)
        return new