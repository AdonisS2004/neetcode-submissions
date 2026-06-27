# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node, height):
            # leaves have a height of 0
            if not node: return True, 0
            # left check
            leftBalanced, leftHeight = helper(node.left, 0)
            if not leftBalanced: return False, 0
            # right check
            rightBalanced, rightHeight = helper(node.right, 0)
            if not rightBalanced: return False, 0

            if abs(leftHeight - rightHeight) > 1: 
                return False, height + 1
            return True, max(leftHeight, rightHeight) + 1
        balanced, _ = helper(root, 0)
        return balanced