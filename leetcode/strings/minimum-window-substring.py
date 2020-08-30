https://leetcode.com/problems/minimum-window-substring

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
            