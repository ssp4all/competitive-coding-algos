"""
Given a root node reference of a BST and a key, 
delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:    return root
        
        def helper(node, k):
            
            def find_min(node):
                while node.left:
                    node = node.left
                return node
            
            if not node:
                return node
            
            if node.val == k:
                if not node.left and not node.right: #child
                    node = None
                    return node
                elif not node.left or not node.right: #either
                    return node.left or node.right
                else:   #both
                    mini = find_min(node.right)
                    node.val = mini.val
                    node.right = helper(node.right, node.val)
                    
                    
            if node.val > k:      
                node.left = helper(node.left, k)
            else:
                node.right = helper(node.right, k)
            return node
        
        return helper(root, key)