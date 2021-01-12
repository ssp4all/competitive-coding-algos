https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
"""

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