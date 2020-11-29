
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root and not arr:    return 1
        if not root or not arr: return 0
        
        def helper(node, ind):
            if not node:    
                return 0
            if ind == len(arr) - 1 and node.val == arr[ind] and not node.left and not node.right:
                return 1
            return (ind < len(arr) and node.val == arr[ind]) and (helper(node.left, ind + 1) or helper(node.right, ind + 1))
        
        return helper(root, 0)