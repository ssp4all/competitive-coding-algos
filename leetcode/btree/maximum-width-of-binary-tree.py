https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:    return 0
        
        dq = collections.deque([(root, 0, 0)])
        ans = 0
        prev = 0
        left = 0
        while dq:
            # print(dq)
            n, d, p = dq.popleft()
            if not n:  
                continue
            
            if prev != d:
                prev = d
                left = p
            ans = max(ans, p - left +1)
            dq.extend([(n.left, d + 1, 2 * p), (n.right, d + 1, 2 * p + 1)])
        # print(lev)
        return ans