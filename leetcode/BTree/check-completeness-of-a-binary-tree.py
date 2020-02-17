https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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