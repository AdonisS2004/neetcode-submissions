# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, prev, count):
            if not node: return count
            total = count
            if node.val >= prev: total += 1
            lcount = helper(node.left, max(node.val, prev), 0)
            rcount = helper(node.right, max(node.val, prev), 0)
            return total + lcount + rcount
        return helper(root, -101, 0)