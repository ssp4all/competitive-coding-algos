https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.
"""

# O(n)
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:    return root
        
        def depth(root):
            if not root:    return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        maxi_depth = depth(root) - 1

        def helper(node, depth):
            if not node:    return
            if depth == maxi_depth:
                return node 
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left and right:
                return node
            return left or right
        return helper(root, 0)

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:    return root
        
        def helper(root):
            if not root:    return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 < h2:
                return h2 + 1, lca2
            if h1 > h2:
                return h1 + 1, lca1 
            return h1 + 1, root 
        return helper(root)[1]
