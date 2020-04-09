https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""
Given a string s and a non-empty string p, find all 
the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the 
length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:   return []
        
        x = Counter(p)
        y = Counter()
        ss = set(p)
        m = 0
        op = []
        n = len(s)
        l, r = 0, n
        cur = 0
        while l < r:
            while cur < r and  cur - l + 1 <= len(p):
                ch = s[cur]
                if ch in ss and y[ch] <= x[ch]:
                    y[ch] += 1
                    m += 1
                if m == len(p):
                    if all(x[i] == y[i] for i in x):
                        op.append(l)
                cur += 1
                
            if s[l] in ss:
                y[s[l]] -= 1
                m -= 1
            l += 1
        return op