# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root in (None, p, q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left is not None else right


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii
"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
"""
 def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while q:
            visited.add(q.val)
            q = q.parent
        
        while p:
            if p.val in visited: return p
            visited.add(p.val)
            p = p.parent
        return None

# upsolving 
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1