# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def diameter(root):
            nonlocal res
            if not root: return 0
            left = diameter(root.left)
            right = diameter(root.right)
            # update res
            opts = max(left + right, left, right)
            res = max(res, opts)
            return max(left, right) + 1
        diameter(root)
        return res





            