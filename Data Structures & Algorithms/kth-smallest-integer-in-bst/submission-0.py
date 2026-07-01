# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node, index_array):
            if not node: return
            helper(node.left, index_array)
            index_array.append(node.val)
            helper(node.right, index_array)
            return
        res = []
        helper(root, res)
        return res[k-1]