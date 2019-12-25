https://leetcode.com/problems/single-number-ii
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int(1.5 * sum(set(nums)) - 0.5 * (sum(nums)))

    def singleNumber(self, nums: List[int]) -> int:
        counter = [0]*32
        ans = 0
        for i in nums:
            for j in range(32):
                if i & (1<<j) != 0:
                    counter[j] += 1
        for j in range(32):
            if counter[j] % 3 != 0:
                ans |= (1<<j)
        return ans
