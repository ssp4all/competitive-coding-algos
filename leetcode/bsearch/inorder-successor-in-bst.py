https://leetcode.com/problems/inorder-successor-in-bst/

"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:    return root
        succ = None
        while root:
            if root.val <= p.val:
                root = root.right 
            else:
                succ = root
                root = root.left
        return succ

#         stack = []
#         while stack or root:
#             while root:
#                 stack += [root]
#                 root = root.left
#             root = stack.pop()
#             if root == p:
#                 root = root.right
#                 if root:
#                     while root.left:
#                         root = root.left 
#                     return root 
#                 else:
#                     while stack and stack[-1].val < p.val:
#                         stack.pop() 
#                     if stack and stack[-1].val > p.val:
#                         return stack.pop()
#                     else:
#                         break
#             root = root.right
            
#         return