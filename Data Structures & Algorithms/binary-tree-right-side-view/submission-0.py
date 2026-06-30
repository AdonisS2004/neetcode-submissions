# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # find depth
        def findDepth(node, depth):
            if not node: return depth
            return max(findDepth(node.left, depth+1), findDepth(node.right, depth+1))
        depth = findDepth(root, 0)
        # create array buffer
        res = [[] for _  in range(depth)]
        # append values dependent on depth
        def createLevel(node, depth):
            if not node: return
            res[depth].append(node.val)
            createLevel(node.left, depth+1)
            createLevel(node.right, depth+1)
        createLevel(root, 0)
        return [res[i][-1] for i in range(depth)]