# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        
        def search(node):
            nonlocal max_sum
            if node is None:
                return 0
            leftSum = search(node.left)
            rightSum = search(node.right)
            possibilities = [
                max_sum,
                node.val,
                node.val + leftSum,
                node.val + rightSum,
                node.val + leftSum + rightSum,
            ]
            max_sum = max(possibilities)
            return max(node.val, node.val+leftSum, node.val+rightSum)

        last = search(root)

        return max(last, max_sum)