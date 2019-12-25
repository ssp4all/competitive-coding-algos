# https://leetcode.com/problems/maximum-depth-of-n-ary-tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if all(not child for child in root.children): return 1
        # print(root.children)
        return 1 + max(self.maxDepth(child) for child in root.children)