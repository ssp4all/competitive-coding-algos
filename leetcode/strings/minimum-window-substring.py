https://leetcode.com/problems/minimum-window-substring

"""
Given a string S and a string T, 
find the minimum window in S which will contain all the characters in T 
in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, 
return the empty string "".
If there is such window, you are guaranteed that there will always
be only one unique minimum window in S.
"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        need = Counter(t)
        
        count = len(need.keys())
        begin, head, end = 0, 0, 0
        size = float('inf')
        while end < len(s):
            if s[end] in need:
                need[s[end]] -= 1
                if need[s[end]] == 0:
                    count -= 1
            end += 1
            while count == 0:
                if s[begin] in need:
                    need[s[begin]] += 1
                    if need[s[begin]] > 0:
                        count += 1
                # print(need)
                if end - begin  < size:
                    size = min(size, end - begin)
                    head = begin
                begin += 1
                
        if size == float('inf'):
            return ""
        return s[head: head + size]

########################################
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:  return ""
        need = Counter(t)
        miss = len(t)
        i, j = 0, 0
        st, end = 0, 0
        for j, ch in enumerate(s, 1):
            if need[ch] > 0:
                miss -= 1
            need[ch] -= 1
            if not miss:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                miss += 1
                if end == 0 or j - i < end - st:
                    st, end = i, j
                i += 1
        return s[st:end]
        
#         n = len(s)
#         if not s or not t: return ""
#         l, r = 0, n - 1
#         anc = 0
#         ans, mini = s, 0
#         count = [float('inf')] * 26
#         inds = set()
#         for i in t:
#             t = ord(i) - ord('A')
#             inds.add(t)
#             if count[t] == float('inf'):
#                 count[t] = 1
#             else:
#                 count[t] += 1
#         print(count, inds)
        
#         def check():
#             return all([count[i] == 0 for i in inds]) == 1
            
#         while l <= r:
#             t = ord(s[l]) - ord('A')
#             if count[t] != float('inf'):
#                 count[t] -= 1
#                 if check():
#                     temp = s[anc : l+1]
#                     if len(ans) > len(temp):
#                         ans = temp
#                 if count[t] < 0:
#                     while not check() and anc <= r:
#                         if s[anc] in : 
#                             count[t] += 1
#                         anc += 1
                    
#             l += 1
#         print(count, anc)
#         return ans
            