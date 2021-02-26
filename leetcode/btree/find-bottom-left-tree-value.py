https://leetcode.com/problems/find-bottom-left-tree-value/

"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Input: root = [2,1,3]
Output: 1
"""

# TC:O(N), SC:O(N)
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val