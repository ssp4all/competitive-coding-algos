https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

# TLE
class Solution:
    def atMostNGivenDigitSet(self, d: List[str], n: int) -> int:
        if not d:   return 0
        # ans = set()
        cnt = 0
        def helper(temp):
            nonlocal cnt
            if len(temp) > len(str(n)):
                return 
            if temp and int(temp) <= n:
                cnt += 1
                # ans.add(int(temp))
            for i in d:
                helper(temp + i)
        helper("")
        return cnt


class Solution:
    def atMostNGivenDigitSet(self, d: List[str], n: int) -> int:
        if not d:   return 0
        s = str(n)
        k = len(s)
        
        dp = [0] * k + [1]
        
        for i in range(k - 1, -1, -1):
            for dd in d:
                if dd < s[i]:
                    dp[i] += len(d) ** (k - i - 1)
                elif dd == s[i]:
                    dp[i] += dp[i + 1]
        return dp[0] + sum(len(d) ** i for i in range(1, k))
        