# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depthHelper(node: Optional[TreeNode], depth: int):
            if not node:
                return depth
            l, r = depthHelper(node.left, depth+1), depthHelper(node.right, depth+1)
            return max(l, r)
        return depthHelper(root, 0)