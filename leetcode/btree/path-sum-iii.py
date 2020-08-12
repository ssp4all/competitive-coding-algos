https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

""" O(n^2) """
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        global ans
        ans = 0
        
        def check(root, sum):
            global ans
            if not root: return
            sum -= root.val
            if sum == 0:
                ans += 1
            check(root.left, sum)
            check(root.right, sum)
        
        def dfs(root, sum):
            if not root: return
            check(root, sum)
            dfs(root.left, sum)
            dfs(root.right, sum)
            
        dfs(root, sum)
        return ans

"""Optimized O(n)"""
# Definition for a binary tree node.w
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:    return 0
        def dfs(node, p):
            if not node: return
            
            p += node.val
            if p-sum in hm:
                self.res += hm[p-sum]
            
            hm[p] += 1
            dfs(node.left, p)
            dfs(node.right, p)
            hm[p] -= 1
            
        hm = defaultdict(int)
        hm[0] = 1
        self.res = 0
        dfs(root, 0)
        return self.res