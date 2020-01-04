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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        global cache, ans
        cache = {0:1}
        ans = 0
        
        def dfs(root, cps, sum):
            global cache, ans
            if not root: return 
            cps += root.val
            ops = cps - sum
            ans += cache.get(ops, 0)
            cache[cps] = cache.get(cps, 0) + 1
            
            dfs(root.left, cps, sum)
            dfs(root.right, cps, sum)
            
            cache[cps] -= 1
        
        dfs(root, 0, sum)
        print(cache)
        return ans