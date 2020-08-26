https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        if not root: return ans
        def preorder(root):
            if not root:    
                ans.append("#")
            else:
                ans.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        # print(ans)
        return " ".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:    return None
        ip = (data.split())
        # print(ip)
        def helper():
            x = next(xx)
            if x == "#":
                return None
            root = TreeNode(int(x))
            root.left = helper()
            root.right = helper()
            return root
        xx = iter(ip)
        return helper()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))