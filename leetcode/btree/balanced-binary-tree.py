https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return 1
        def height(root):
            if not root: return 0
            le = height(root.left)
            ri = height(root.right)
            if le == -1 or ri == -1 or abs(le-ri) > 1:
                return -1
            return 1 + max(le, ri)
        return height(root) != -1