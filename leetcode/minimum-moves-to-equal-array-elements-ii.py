https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from collections import Counter
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        xx = Counter(nums)
        li = list(xx.items())
        ans = 99**99
        print(li)
        for i, j in li:
            temp = 0
            for m, n in li:
                if i == m:  continue
                temp += (abs(i - m) * n)
            ans = min(ans, temp)
        return ans

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2
        ans = 0
        for i in nums:
            ans += (abs(i - nums[mid]))
        return ans