https://leetcode.com/problems/convert-bst-to-greater-tree/
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

"""
Given the root of a Binary Search Tree (BST), convert it to a Greater 
Tree such that every key of the original BST is changed to the original 
key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the 
node's key.
The right subtree of a node contains only nodes with keys greater than 
the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

"""
# TC:O(N)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        tot = 0
        
        def helper(node):
            nonlocal tot
            if not node:    return 
            helper(node.right)
            tot += node.val
            node.val = tot
            helper(node.left)
            
        helper(root)
        return root