https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if (not s and t) or (not t and s): return False
        
        def isSame(s, t):
            if not s and not t: return True
            if (not s and t) or (not t and s):
                return False
            return (s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right))
        
        if s.val == t.val:
            if isSame(s, t):
                return True
        return self.isSubtree(s.right, t) or self.isSubtree(s.left, t)
        
#         if s is None and t is None: return True
#         if s.left: 
#             if self.isSubtree(s.left, t):
#                 return True
#         if s.right:
#             if self.isSubtree(s.right, t):
#                 return True

#         if s.val == t.val:
#             return self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)
        
#         if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
#             return True
#         return False

        
        
        