https://leetcode.com/problems/add-one-row-to-tree/

"""
Given the root of a binary tree, then value v and depth d, 
you need to add a row of nodes with value v at the given depth d. 
The root node is at depth 1.

A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2
"""
# TC:O(N), SC:O(H)
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        
        def helper(node, depth):
            if not node:    return 
            
            if depth == d - 1:
                left_ptr = node.left 
                node.left = TreeNode(v)
                node.left.left = left_ptr
                right_ptr = node.right 
                node.right = TreeNode(v)
                node.right.right = right_ptr
                return 
            
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
            
            return node
        
        helper(root, 1)
        return root