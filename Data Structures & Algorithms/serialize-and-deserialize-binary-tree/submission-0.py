# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def encoder(self, node, s_list):
        if node.left:
            s_list.append('l')
            self.encoder(node.left, s_list)
        if node.right:
            s_list.append('r')
            self.encoder(node.right, s_list)
        s_list.append(str(node.val))
        s_list.append('u')
        return

    def decoder(self, s, i):
        node = TreeNode()
        if s[i] == 'l':
            node.left, i = self.decoder(s,i+1)
        if s[i] == 'r':
            node.right, i = self.decoder(s,i+1)
        val = []
        while s[i] not in {'l', 'r', 'u'}:
            val.append(s[i])
            i += 1
        node.val = int("".join(val))
        return node, i+1

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        res = []
        self.encoder(root, res)
        return "".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None
        root, _ = self.decoder(data, 0)
        return root