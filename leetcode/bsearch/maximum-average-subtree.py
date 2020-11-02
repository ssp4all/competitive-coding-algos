https://leetcode.com/problems/maximum-average-subtree/

"""
Given the root of a binary tree, find the maximum average value of any subtree of that tree.
(A subtree of a tree is any node of that tree plus all its descendants. 
The average value of a tree is the sum of its values, divided by the number of nodes.)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:    return 0
        ans = float('-inf')
        
        def helper(node):
            nonlocal ans
            if not node:
                return [0, 0]
            if not node.left and not node.right:    
                if ans < node.val:
                    ans = max(ans, node.val)
                    return [node.val, 1]
            
            sum_, cnt = node.val, 1
            for child in [node.left, node.right]:
                s, c = helper(child)
                sum_ += s
                cnt += c
                
            if ans < sum_ / cnt:
                ans = max(ans, sum_ / cnt)
                
            return [sum_, cnt]
        
        helper(root)
        return ans