# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:    return root
        
        le = self.invertTree(root.left)
        ri = self.invertTree(root.right)
        
        
        # temp = root.left
        root.left = ri
        root.right = le
        
        return root