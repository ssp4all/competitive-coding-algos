https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: return 0
        n = len(s)
        l, r = 0, n - 1
        j = 0
        cache = dict()
        ans = 0
        while l <= j and j <= r:
            if s[j] in cache:
                cache[s[j]] += 1
            else:
                cache[s[j]] = 1
            ll = len(cache.keys())
            if ll <= k:
                ans = max(ans, j - l + 1)
            else:
                while l <= j and len(cache.keys()) > k:
                    if cache[s[l]] > 1:
                        cache[s[l]] -= 1
                    else:
                        del cache[s[l]]
                    l += 1
            j += 1
        return ans
                
                
            