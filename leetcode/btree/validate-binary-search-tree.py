https://leetcode.com/problems/validate-binary-search-tree

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
"""
class Solution:
    def isValidBST(self, root: TreeNode, left=float('-inf'), right=float('inf')) -> bool:
        return not root or left < root.val < right and \
                self.isValidBST(root.left, left, root.val) and \
                    self.isValidBST(root.right, root.val, right)

import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:    return 1
        q = [(root, -math.inf, math.inf)]
        while q:
            node, l, h = q.pop()
            if not node:    continue
            v = node.val
            if v <= l or v >= h:    return 0
            q.extend([(node.right, v, h), (node.left, l, v)])
        return 1