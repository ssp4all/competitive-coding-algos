# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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