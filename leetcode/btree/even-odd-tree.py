https://leetcode.com/problems/even-odd-tree/

"""
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, 
their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in 
strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values 
in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, 
otherwise return false.


"""
from collections import deque

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:    return 0
        
        dq = deque([root])
        d = 0
        while dq:
            size = len(dq)
            odd, even = [], []
            tmp = []

            for _ in range(size):
                node = dq.popleft()
                if not node:    continue

                if d & 1 == 1:
                    if not odd and node.val & 1 == 0:
                        odd += [node.val]
                    elif odd and odd[-1] > node.val and node.val & 1 == 0:
                        odd += [node.val]
                    else:
                        return 0
                else:
                    if not even and node.val & 1 == 1:
                        even += [node.val]
                    elif even and even[-1] < node.val and node.val & 1 == 1:
                        even += [node.val]
                    else:
                        return 0
                tmp += [node.left, node.right]
            d += 1
            dq = deque(tmp)
        return 1