# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return nums[n-1]

# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        l, r = [0]*(n - 1), [0]*(n)
        if n == 1:  return nums[0]
        elif n == 2:  return max(nums[0], nums[1])
        # elif n == 3:    return nums[1]
        l[0], r[1] = nums[0], nums[1]
        l[1] = max(nums[0], nums[1])
        r[2] = max(nums[1], nums[2])
        for i in range(2, n - 1):
            l[i] = max(l[i - 1], nums[i] + l[i - 2])
        # print(l)
        for i in range(3, n):
            r[i] = max(r[i - 1], nums[i] + r[i - 2])
        # print(r)
        return max(l[-1], r[-1])

# https://leetcode.com/problems/house-robber-iii
"""
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." Besides the root,
 each house has one and only one parent house. After a tour, the smart thief realized 
 that "all houses in this place forms a binary tree". It will automatically contact the 
 police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
"""
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:    return 0 
        @functools.lru_cache(None)
        def helper(node, status):
            if not node:    return 0

            a = (node.val if status else 0) + \
                    helper(node.left, not status) + \
                        helper(node.right, not status) 
            b = helper(node.left, status) + \
                        helper(node.right, status)
            return max(a, b)
            
        return max(helper(root, 0), helper(root, 1))
# O(n)
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:    return 0 
        
        @functools.lru_cache(None)
        def helper(node):
            if not node:    return (0, 0)
            
            left = helper(node.left)
            right = helper(node.right)
            
            rob = node.val + left[1] + right[1]
            
            not_rob = max(left) + max(right)
        
            return (rob, not_rob)
        
        return max(helper(root))