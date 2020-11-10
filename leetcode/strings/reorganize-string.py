https://leetcode.com/problems/reorganize-string/

"""
Given a string S, check if the letters can be rearranged so that two characters 
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
"""

from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:   return ""
        xx = Counter(s)
        ip = list(map(list, xx.items()))
        # print(ip)
        global op
        def bt(ans):
            global op
            # print(ans, ip)
            ip.sort(key=lambda x:(-x[1]))
            if ip[0][1] <= 0:
                op = ans
                return 1
            else:
                for ind, (i, j) in enumerate(ip):
                    if not ans or (ans[-1] != i and j > 0):
                        ip[ind][1] -= 1
                        if bt(ans + [i]):   return 1
                        ip[ind][1] += 1
                return 0
        op = []
        bt([])
        return "".join(op)

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:   return ""
        n = len(s)
        op = []
        for c, x in sorted((s.count(x), x) for x in set(s)):
            if c > (n + 1) / 2: return ""
            op.extend(c * x)
        # print(op)
        ans = [None] * n
        ans[::2], ans[1::2] = op[n//2:], op[:n//2]
        return "".join(ans)
             
        