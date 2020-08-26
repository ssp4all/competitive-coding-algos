https://leetcode.com/problems/insert-into-a-binary-search-tree/

"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:    return TreeNode(val)
        
#         def helper(node, val):
#             if not node:
#                 return TreeNode(val)
            
#             if node.val > val:
#                 node.left = helper(node.left, val)
#             else:
#                 node.right = helper(node.right, val)

#             return node
            
            
#         return helper(root, val)
        node = root
        while True:
                
            if node.val > val:
                
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right

            
        return root