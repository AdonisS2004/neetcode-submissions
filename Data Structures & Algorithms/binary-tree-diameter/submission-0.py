# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # current diameter, height
        def findDiameter(node: Optional[TreeNode], depth: int) -> (int, int):
            if not node: return depth, 0
            leftDiam, leftHeight = findDiameter(node.left, depth)
            rightDiam, rightHeight = findDiameter(node.right, depth)
            head2toe = depth + max(leftHeight, rightHeight) - 1
            toe2toe = leftHeight + rightHeight
            return max(leftDiam, rightDiam, head2toe, toe2toe), max(leftHeight, rightHeight) + 1
        diameter, _ = findDiameter(root, 0)
        return diameter






            