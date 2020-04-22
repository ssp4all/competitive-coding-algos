https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

import math
class Solution:
    def isValidBST(self, root: TreeNode, l = -math.inf, u = math.inf) -> bool:
        if not root:    return 1
        return l < root.val < u \
            and (self.isValidBST(root.left, l, root.val) \
                    and self.isValidBST(root.right, root.val, u))