https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:    return nums
        n = len(nums)
        op = []
        prod = 1
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
                continue
            prod *= i
        if zero == 1:
            for i in nums:
                if i == 0:
                    op.append(prod)
                else:
                    op.append(0)
        elif zero > 1:
            op = [0] * n
        else:
            for i in nums:
                op.append(prod // i)
        return op