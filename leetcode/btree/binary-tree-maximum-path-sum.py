https://leetcode.com/problems/binary-tree-maximum-path-sum

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes 
from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Nonew

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:    return 0       
        global ans
        ans = float('-inf') 
        
        def helper(node):
            global ans

            if not node:
                return 0
            # print(node.val, ans)

            l = max(0, helper(node.left))
            r = max(0, helper(node.right))
            summ = l + r + node.val
            ans = max(ans, summ)
            return max(l, r) + node.val
            
            
        x = helper(root)
        ans = max(ans, x)
        return root.val if ans == float('-inf') else ans