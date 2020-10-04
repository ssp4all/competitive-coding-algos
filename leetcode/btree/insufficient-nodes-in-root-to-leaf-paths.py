https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

"""
Given the root of a binary tree, consider all root to leaf paths:

paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting 
this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.
"""

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:    return root
        
        def helper(node, limit):
            if not node.left and not node.right:    
                if node.val < limit:    
                    return None
                else:
                    return node
            if node.left:
                node.left = helper(node.left, limit - node.val)
            if node.right:
                node.right = helper(node.right, limit - node.val)
                
            if not node.left and not node.right:
                return None
            return node
        return helper(root, limit)
    
    
    
        # l = helper(node.left, node.val + tot)
        # r = helper(node.right, node.val + tot) 
        # if l < limit and r < limit:
        #     node.left, node.right = None, None
        #     return tot + node.val
        # if l < limit:
        #     node.left = None
        # if r < limit:
        #     node.right = None
        # return (l if l >= limit else 0) + (r if r >= limit else 0)
