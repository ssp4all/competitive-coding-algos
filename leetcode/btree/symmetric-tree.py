# https://leetcode.com/problems/symmetric-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def isMirror(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val == b.val:
                return isMirror(a.left, b.right) and isMirror(a.right, b.left)
            else:
                return False
        return isMirror(root.left, root.right)
    
        