https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent. 
 (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
"""

# TC:O(N), SC:O(H)
class Solution:
	def helper(node, parent, grandparent):
        total = 0
        if not node:
            return 0
        if grandparent and (grandparent.val % 2 == 0):
            total += node.val
        total += helper(node.left, node, parent)
        total += helper(node.right, node, parent)
        return total
        
        
    return helper(root, None, None)