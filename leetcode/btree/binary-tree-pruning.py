https://leetcode.com/problems/binary-tree-pruning/

"""
We are given the head node root of a binary tree, where additionally 
every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not 
containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that 
is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
"""


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:    return root 
        
        
        def helper(node):
            #returns a true if found 1
            if not node:    return 0
            
            left = helper(node.left)
            if left == 0:
                node.left = None
            right = helper(node.right)
            if right == 0:
                node.right = None
                            
            return node.val == 1 or left or right
        
        helper(root)
        return root if helper(root) == 1 else None

#upsolving 
class Solution(object):
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None