https://leetcode.com/problems/recover-binary-search-tree/

"""
You are given the root of a binary search tree (BST), where exactly two nodes 
of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise 
a constant space solution?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        #inorder
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    
        # find two miss placed
        def missplaced(arr):
            n = len(arr)
            x, y = [-1, -1]
            
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    y = arr[i + 1]
                    if x == -1:
                        x = arr[i]
                    else:
                        break        
            return [x, y]
        
        def recover(node, count):
            if not node:    return 
            if node.val in [x, y]:
                node.val = y if node.val == x else x
                count -= 1
                if count == 0:
                    return 
            recover(node.left, count)
            recover(node.right, count)
        
        arr = inorder(root)
        x, y = missplaced(arr)
        recover(root, 2)
#######################################################
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = prev = None
        
        while stack or root:
            while root:
                stack += [root]
                root = root.left
            
            root = stack.pop()
            if prev and prev.val > root.val:
                x = root
                if y is None:
                    y = prev
                else:
                    break
        
            prev = root
            root = root.right
        x.val, y.val = y.val, x.val


                