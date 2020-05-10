https://leetcode.com/problems/cousins-in-binary-tree/

"""
In a binary tree, the root node is at depth 0, 
and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have 
the same depth, but have different parents.

We are given the root of a binary tree with unique values, 
and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the 
values x and y are cousins.


"""

import collections
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:    return 0
        
        dq = collections.deque([(root, 0, None)])
        cache = dict()
        while dq:
            node, d, p = dq.popleft()
            if not node:    continue 
            cache[node.val] = (d, p)
            dq.extend([(node.left, d + 1, node.val), (node.right, d + 1, node.val)])
            
        return cache[x][0] == cache[y][0] and cache[x][1] != cache[y][1]