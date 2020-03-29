https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

"""
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level 
order traversal of its nodes' values. (ie, from left to right, 
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque([(root, 0)])
        levels = []
        while dq:
            n, d = dq.popleft()
            if not n:
                continue
            if len(levels) == d:
                levels.append([])
            levels[d].append(n.val)
            dq.extend([(n.left, d + 1), (n.right, d + 1)])
            
        for i, l in enumerate(levels):
            if i % 2 == 0:
                continue
            levels[i] = levels[i][::-1]
        return levels
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque([(root, 0)])
        levels = collections.deque()
        l = 0
        while dq:
            n, d = dq.popleft()
            if not n:
                continue
            if len(levels) == d:
                levels.append(deque())
                l = not l

            if l:
                levels[d].append(n.val)
            else:
                levels[d].appendleft(n.val)
                # l = not l
            dq.extend([(n.left, d + 1), (n.right, d + 1)])
            
        # for i, l in enumerate(levels):
        #     if i % 2 == 0:
        #         continue
        #     levels[i] = levels[i][::-1]
        return levels
                