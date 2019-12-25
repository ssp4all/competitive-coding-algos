# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels
        
        # depth = 0
        def dfs(root, depth):
            if not root: return levels
            if len(levels) == depth:
                levels.append([])
                
            levels[depth].append(root.val)
            if root.left:
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)
            return levels
        dfs(root, 0)
        return levels