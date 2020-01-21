https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

import collections

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            # print(cur)
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
                # print(res)
            while d and cur <= d[-1][1]:
            	d.pop()
            d.append([i + 1, cur])
            # print(d)
        return res if res < float('inf') else -1