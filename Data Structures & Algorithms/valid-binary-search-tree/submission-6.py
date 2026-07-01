# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, minimum, maximum):
            if node == None: return True
            if minimum is not None and node.val <= minimum: return False
            if maximum is not None and node.val >= maximum: return False
            # update minimum and maxium
            return helper(node.left, minimum, node.val) and helper(node.right, node.val, maximum)
        return helper(root, None, None)
            