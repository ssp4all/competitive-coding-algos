
"""
Given a binary tree, return the vertical order traversal 
of its nodes values.

For each node at position (X, Y), its left and right children 
respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, 
whenever the vertical line touches some nodes, 
we report the values of the nodes in order from top to 
bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the 
node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  
Every report will have a list of values of nodes.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:    return []
        
        op = collections.defaultdict(list)
        
        dq = [(root, 0)]
        while dq:
            temp = []
            g = collections.defaultdict(list)
            for n, p in dq:
                if not n:   continue
                g[p].append(n.val)
                temp.extend([(n.left, p - 1), (n.right, p + 1)])
            for i in g:
                op[i].extend(sorted(g[i]))
            dq = temp
        return [op[i] for i in sorted(op)]
            
           