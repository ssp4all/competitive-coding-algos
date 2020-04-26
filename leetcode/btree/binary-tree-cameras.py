https://leetcode.com/problems/binary-tree-cameras/

"""
Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:    
            return 0
        seen = {None}
        ans = 0
        def helper(root, p):
            nonlocal ans
            if not root:
                return 
            helper(root.left, root)
            helper(root.right, root)
            if (not p and root not in seen) or \
                root.left not in seen or \
                    root.right not in seen:
                ans += 1
                seen.update({p, root, root.left, root.right})
            
            
        helper(root, None)
        return ans