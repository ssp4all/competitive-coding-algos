https://leetcode.com/problems/trim-a-binary-search-tree/


"""
Given the root of a binary search tree and the lowest 
and highest boundaries as low and high, trim the tree so 
that all its elements lies in [low, high]. Trimming the tree 
should not change the relative structure of the elements that will
 remain in the tree (i.e., any node's descendant should remain a descendant).
 It can be proven that there is a unique answer.
"""

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:    return root 

        def dfs(node):
            if not node:    return node
            if low <= node.val <= high:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
            else:
                if node.val < low:
                    return dfs(node.right)
                return dfs(node.left)
        return dfs(root)

# upsolving
class Solution(object):
    def trimBST(self, root, low, high):

        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)