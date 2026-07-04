# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = root, left, right
        # inorder = left, root, right
        # bisection seach on inorder for left and right divisions 
        if not preorder: return None
        # helpers
        indices = {value:idx for idx, value in enumerate(inorder)}
        def build(pre_ptr, in_l, in_r):
            if in_l > in_r: return None
            # update node.val
            node = TreeNode()
            node.val = preorder[pre_ptr]
            # update pointers
            in_ptr = indices[preorder[pre_ptr]]
            pre_l = pre_ptr + 1
            pre_r = pre_ptr + 1 + abs(in_ptr - in_l)
            # get left and right
            node.left = build(pre_l, in_l, in_ptr-1)
            node.right = build(pre_r, in_ptr+1, in_r)
            return node
        return build(0, 0, len(preorder)-1)