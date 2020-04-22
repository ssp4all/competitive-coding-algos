https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

"""
Return the root node of a binary search tree that matches 
the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, 
any descendant of node.left has a value < node.val, and any descendant 
of node.right has a value > node.val.  Also recall that a preorder 
traversal displays the value of the node first, then traverses node.left, 
then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12] 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:    return None
        
        inorder = sorted(preorder)
        
        def helper(arr):
            if not arr: return None
            val = preorder.pop(0)
            ind = arr.index(val)
            root = TreeNode(val)
            root.left = helper(arr[:ind])
            root.right = helper(arr[ind + 1:])
            
            return root
        return helper(inorder)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:    return None
        
        inorder = sorted(preorder)
        idx = 0
        def helper(arr):
            nonlocal idx
            if not arr: return None
            val = preorder[idx]
            idx += 1
            ind = arr.index(val)
            root = TreeNode(val)
            root.left = helper(arr[:ind])
            root.right = helper(arr[ind + 1:])
            
            return root
        return helper(inorder)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:    return None
        
        idx = 0
        def helper(l = float('-inf'), u = float('inf')):
            nonlocal idx
            if idx == len(preorder):
                return None
            val = preorder[idx]
            if not( l < val < u):
                return None                
            idx += 1            
            root = TreeNode(val)
            root.left = helper(l, val)
            root.right = helper(val, u)
            
            return root
        return helper()