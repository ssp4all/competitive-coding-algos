# https://leetcode.com/problems/symmetric-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def isMirror(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val == b.val:
                return isMirror(a.left, b.right) and isMirror(a.right, b.left)
            else:
                return False
        return isMirror(root.left, root.right)
    
# https://leetcode.com/problems/same-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  return 1
        if not p or not q:     return 0
        def helper(root):
            if not root:    return "#"
            serial = f"{root.val}{helper(root.left)}{helper(root.right)}"
            return serial
        return helper(p) == helper(q)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return 1
        if not p or not q: return 0
        return (p.val == q.val) and \
                self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)
 
"""Using iteration """
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return 1
        if not p or not q: return 0
        def bfs(a):
            stack, op = [], []
            stack.append(a)
            while len(stack) != 0:
                node = stack.pop(0)
                if not node:
                    op.append(None)
                    continue
                else:
                    op.append(node.val)
                    
                if not node.left:
                    stack.append(None)
                else:
                    stack.append(node.left)

                if not node.right:
                    stack.append(None)
                else:
                    stack.append(node.right)
                
                print(op)
            return op
        return bfs(p) == bfs(q)