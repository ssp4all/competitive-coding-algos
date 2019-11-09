# @author: Suraj Pawar

# https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]*nums[-2]*nums[-3]
        b = nums[-1]*nums[1]*nums[0]
        c = nums[0]*nums[-2]*nums[-3]
        return max(a, b, c)