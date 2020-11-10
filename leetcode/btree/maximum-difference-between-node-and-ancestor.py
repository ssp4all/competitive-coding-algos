https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

"""
Given the root of a binary tree, find the maximum value V for 
which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, 
or any child of A is an ancestor of B.

 
"""
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:    return 0
        ans = float('-inf')
        
        def dfs(root, mini, maxi):
            nonlocal ans
            if not root:    return
            
            mini = min(mini, root.val)
            maxi = max(maxi, root.val)
            ans = max(ans, abs(maxi - root.val), abs(root.val - mini))
            dfs(root.left, mini, maxi)
            dfs(root.right, mini, maxi)
            
        dfs(root, float('inf'), float('-inf'))
        return ans

# Editorial
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)