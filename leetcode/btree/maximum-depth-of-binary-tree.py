# https://leetcode.com/problems/maximum-depth-of-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        # if not root.left and not root.right: return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# For minimum depth
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:    return 0
        def helper(root):
            if not root:    return float('inf')
            if not root.left and not root.right:
                return 1
            return 1 + min(helper(root.left), helper(root.right))
        return helper(root)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:    return 0
        
        q = collections.deque([(root, 1)])
        while q:
            node, d = q.popleft()
            if not node:
                continue
            if not node.left and not node.right:
                return d
            q.extend([(node.left, d + 1), (node.right, d + 1)])