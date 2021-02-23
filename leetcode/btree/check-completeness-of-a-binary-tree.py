https://leetcode.com/problems/check-completeness-of-a-binary-tree/


"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is 
completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Input: root = [1,2,3,4,5,6]
Output: true
"""

from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:    return 0
        que = deque([root])
        while que[0]:
            node = que.popleft()
            que.append(node.left)
            que.append(node.right)
        while que and not que[0]:
            que.popleft()
        return not que