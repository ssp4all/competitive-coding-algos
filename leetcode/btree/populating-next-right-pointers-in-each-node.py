https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        levels = [[root]]
        def helper(root, depth):
            if not root: return 
            if len(levels) == depth:
                levels.append([])
            levels[depth].append(root)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        
        
        helper(root.left, 1)
        helper(root.right, 1)
        
        # print(levels)
        
        for i in range(len(levels)):
            if len(levels[i]) == 1:
                levels[i][0].next = None
            else:
                ll = len(levels[i])
                for j in range(ll-1):
                    levels[i][j].next = levels[i][j+1]
                levels[i][ll-1].next = None
        return root