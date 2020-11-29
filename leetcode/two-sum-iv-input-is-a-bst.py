https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return 0
        op = []
        def helper(root):
            if not root: return 
            helper(root.left)
            op.append(root.val)
            helper(root.right)
        helper(root)
        
        d = {val:i for i, val in enumerate(op)}
        for i in range(len(op)):
            if k-op[i] in d: 
                if d[k-op[i]] != i:
                    return 1
        return 0
        

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            temp = nums[l]+nums[r]
            # print(temp)
            if temp == k:
                return [l+1, r+1]
            elif temp < k:
                l += 1
            else:
                r -= 1
        return []