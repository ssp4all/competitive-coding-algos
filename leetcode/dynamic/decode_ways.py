https://leetcode.com/problems/decode-ways/submissions/

class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(ss):
            print(ss)
            if not ss:   
                return 1
            else:
                if ss[0] == "0":
                    return 0
                return helper(ss[1:]) + \
                    (helper(ss[2:]) if (0 < int(ss[:2]) < 27 and len(ss[:2]) >=2) else 0)

        return helper(s)

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def helper(ss):
            if ss in cache: return cache[ss]
            
            if not ss:   
                return 1
            else:
                if ss[0] == "0":
                    return 0
                res = helper(ss[1:])
                if 0 < int(ss[:2]) < 27 and len(ss[:2]) >= 2:
                    res += helper(ss[2:])
                cache[ss] = res
                return res
        return helper(s)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        if not s or int(s[0]) == 0:
            return 0
        dp = [0] * (n+1)
        dp[:2] = [1]*2
        for i in range(2, n+1):
            
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
                
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]