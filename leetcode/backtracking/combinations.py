https://leetcode.com/problems/combinations/

from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n: return []
        return combinations(list(range(1, n+1)), k)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n: return []
        nums = list(range(1, n+1))
        ans = set()
        def bt(temp, no, st):
            if no == 0:
                ans.add(tuple(temp))
            else:
                for i in range(st, n):
                    bt(temp + [nums[i]], no - 1, i+1)
        bt([], k, 0)
        return ans